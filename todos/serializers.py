from rest_framework import serializers
from .models import TodoModel

class TodoModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = TodoModel
        fields = '__all__'


# protecting against os command injection
    def validate_task(self,value):
        forbidden_characters = ['`','>','<','&','|',';','!']
    # do not allow to save a user if it contains os command injection characters       
        if any(char in value for char in forbidden_characters):
            raise serializers.ValidationError(detail=f"The following characters are forbidden in the username: {', '.join(forbidden_characters)}.")

        return value
    

 