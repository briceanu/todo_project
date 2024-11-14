from rest_framework import serializers
from .models import UserModel
import re


class UserSerialzier(serializers.ModelSerializer):
    confirm_password = serializers.CharField(write_only=True)

    class Meta:
        model = UserModel
        fields = ['user_id','username','email','password','last_login','date_joined','confirm_password']



    def validate_username(self,value):
        forbidden_characters = ['`','>','<','&','|',';','!']
    # do not allow to save a user if it contains os command injection characters       
        if any(char in value for char in forbidden_characters):
            raise serializers.ValidationError(detail=f"The following characters are forbidden in the username: {', '.join(forbidden_characters)}.")
        if len(value) <= 6 :
            raise serializers.ValidationError(detail='Username must be at least 6 characters')
        return value
    

    def validate_password(self,value):
        # validating password constraints
        if not re.search(r'[A-Z]',value):
            raise serializers.ValidationError("Password must contain at least one uppercase letter")
        
        if not re.search(r'\d',value):
            raise serializers.ValidationError(detail='Password must contain at least one number')
        
        if len(value) <= 6 :
            raise serializers.ValidationError(detail='Password must be at least 6 characters')
        return value
    
    def validate(self,data):
        # checking to see if the passwords match
        if data.get('confirm_password') != data.get('password'):
            raise serializers.ValidationError(detail='Passwords do not match')

        if UserModel.objects.filter(username=data.get('username')).exists():
            raise serializers.ValidationError(detail='Username already exists')
        return data
    

    def create(self, validated_data):
        # extracting the confirm_password
        validated_data.pop('confirm_password')
        # creating the data 
        user = UserModel.objects.create(**validated_data)
        # hashing the password
        user.set_password(validated_data['password'])
        # saving the user
        user.save()
        return user