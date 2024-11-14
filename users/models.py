from django.db import models
from django.contrib.auth.models import AbstractUser
import uuid



class UserModel(AbstractUser):
    user_id = models.UUIDField(primary_key=True,default=uuid.uuid4,editable=False)
    date_joined = models.DateTimeField(auto_now_add=True)
    username = models.CharField(unique=True,null=False, max_length=40)
    email = models.EmailField(unique=True,null=False)

