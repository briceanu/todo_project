from rest_framework import generics
from rest_framework.decorators import APIView ,api_view, permission_classes
from .models import UserModel
from .serializers import UserSerialzier
from rest_framework.response import Response
from rest_framework import status
from rest_framework.authentication import authenticate
from .tokens import get_tokens_for_user 
from rest_framework_simplejwt.tokens import RefreshToken 
from rest_framework_simplejwt.exceptions import TokenError
from .tokens import get_new_access_token_for_user
from rest_framework import mixins
from rest_framework.permissions import IsAdminUser, IsAuthenticated 
from rest_framework.exceptions import NotFound
from rest_framework import viewsets
from django.contrib.auth.hashers import make_password


# class used by ADMIN
class ListUsersAPI(generics.ListAPIView):
    # permission_classes = [IsAdminUser]
    # only and admin ca see all the users
    queryset = UserModel.objects.all()
    serializer_class = UserSerialzier

# class used by ADMIN
class RemoveUserAPI(generics.DestroyAPIView):
    permission_classes = [IsAdminUser]

    def delete(self,request):
        username = request.data.get('username')
        if not username:
            return Response({'error': 'No username provided'}, status=status.HTTP_400_BAD_REQUEST)
        # get the user or throw a 404 not found is the user does not exist
        try:
            user = UserModel.objects.get(username=username)
        except UserModel.DoesNotExist:
            raise NotFound(detail=f'no user with the username {username} found')
        
        try:
            # remove the user and send a 200 OK to the 
            user.delete()
            return Response({'success':f'user {user}removed'},status=status.HTTP_200_OK)
        except Exception as e:
            return Response({'error':str(e)},status=status.HTTP_500_INTERNAL_SERVER_ERROR)





# creating a new user
class SignUpAPI(APIView):
    def post(self,request):
        try:
            serializers = UserSerialzier(data=request.data)
            # check to see if the data is valid
            if serializers.is_valid():
            # if the data is valid save it in the db
                serializers.save()
                return Response({'user created':serializers.data},status=status.HTTP_201_CREATED)
            return Response({'error':serializers.errors},status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response({'error':str(e)},status=status.HTTP_500_INTERNAL_SERVER_ERROR)


# signin a user 
class SignInAPI(APIView):
    def post(self,request):
        try:
            # getting the username and password from the request body
            password = request.data.get('password')
            username = request.data.get('username')
            # authenticating the user using the username and the password 
            user = authenticate(username=username,password=password)
            if user is None:
                return Response(
                    {'forbidden':'username or password do not match'},
                    status=status.HTTP_403_FORBIDDEN
                )
            # returning tokens after checking the user credentials  
            tokens = get_tokens_for_user(user)
            return Response(tokens,status=status.HTTP_200_OK)
        
        except Exception as e:
            return Response({"error":str(e)},status=status.HTTP_500_INTERNAL_SERVER_ERROR)


# providing a new access token 

class NewAccessTokenAPI(generics.CreateAPIView):
#    permission_classes = [IsAuthenticated]

   def post(self, request):
        # Extract the authorization header
        refresh_token = request.headers.get('Authorization')
        
        # Check if token is provided and well-formed
        if not refresh_token or not refresh_token.startswith('Bearer '):
            return Response(
                {"error": "No refresh token provided"},
                status=status.HTTP_400_BAD_REQUEST
            )
        
        # Extract the actual token part
        refresh_token = refresh_token.split(' ')[1]
        
        try:
            # Attempt to create a RefreshToken object
            refresh = RefreshToken(refresh_token)
            username = refresh.get('username')
            
            # Check if the user exists
            user = UserModel.objects.filter(username=username).first()
            if user is None:
                return Response(
                    {"error": "Forbidden"},
                    status=status.HTTP_403_FORBIDDEN
                )
            
            # Generate a new access token
            access_token = {'access': get_new_access_token_for_user(user)}
            return Response(access_token, status=status.HTTP_200_OK)

        except TokenError:
            # TokenError is raised if the token is invalid or expired
            return Response(
                {"error": "Forbidden"},
                status=status.HTTP_403_FORBIDDEN
            )


# logout and blacklist the token
class LogoutAPI(generics.GenericAPIView,mixins.CreateModelMixin):
    def post(self, request, *args, **kwargs):
        try:
            # Get the refresh token from the request body
            refresh_token = request.data.get('refresh_token')
            if not refresh_token:
                return Response({'error': 'No refresh token provided'}, status=status.HTTP_400_BAD_REQUEST)

            # Attempt to blacklist the refresh token
            token = RefreshToken(refresh_token)
            token.blacklist()

            return Response({'success': 'Token blacklisted'}, status=status.HTTP_200_OK)

        except TokenError:
            return Response({"error": "Token is invalid or already blacklisted"}, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        




# patch to update only the password
@api_view(['PATCH'])
@permission_classes([IsAuthenticated])
def update_user_password(request):
    # get the username form the token
    username = request.user.username
    # get the user using the username extracted from the token
    def get_user():
        try:
            return UserModel.objects.get(username=username)
        except UserModel.DoesNotExist:
            raise NotFound(detail=f'No user with username {username} found.')

    password = request.data.get('password')
    confirm_password = request.data.get('confirm_password') 
    # validating if the client has provided both password and confirm_password
    if not password or not confirm_password:
        return Response({'error':'no password or confirm_password provided'},status=status.HTTP_400_BAD_REQUEST)
        # checking to see if the passwords match
    if password != confirm_password:
        return Response({'error':'passwords do not match'},status=status.HTTP_400_BAD_REQUEST)
    user = get_user()
    data = {'password': password,'confirm_password': confirm_password}
    # serializing the data
    serializer = UserSerialzier(user, data=data, partial=True)
        # checking to see if the data is valid
    if serializer.is_valid():
        # hasing the password
        user.password = make_password(password)       
        user.save() 
        return Response({'user data updated': serializer.data}, status=status.HTTP_200_OK)
    return Response({'error':serializer.errors},status=status.HTTP_400_BAD_REQUEST)





# update all the user data
class UpdateUserDataAPI(viewsets.ViewSet):
    
    permission_classes = [IsAuthenticated]
    # getting the object that belongs to the logged in user 
    def get_object(self):
        username = self.request.user.username
        try:
            return UserModel.objects.get(username=username)
        except UserModel.DoesNotExist:
            raise NotFound(detail=f'no user with the username {username} found.')

    def update(self, request):
        password = request.data.get('password')
        confirm_password = request.data.get('confirm_password') 
        # checking to see if the client has provided password and confirm_password
        if not password or not confirm_password:
            return Response({'error':'no password or confirm_password provided'},status=status.HTTP_400_BAD_REQUEST)
        # checking to see if the passwords match
        if password != confirm_password:
            return Response({'error':'passwords do not match'},status=status.HTTP_400_BAD_REQUEST)
    
        user = self.get_object()
        # passing the data from the request body to the UserSerializer
        serializer = UserSerialzier(user,data=request.data)
        # checking to see if the data is valid
        if serializer.is_valid():
            # Hash the password
            user.set_password(password)
            # if the data is valid save it
            serializer.save() 
            return Response({'user data updated': serializer.data}, status=status.HTTP_200_OK)
        # if the data is not valid throw a 400 bag request 
        return Response({'error':serializer.errors},status=status.HTTP_400_BAD_REQUEST)




    