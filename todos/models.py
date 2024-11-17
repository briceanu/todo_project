from django.db import models
import uuid
from users.models import UserModel



class TodoModel(models.Model):
    task_id = models.UUIDField(primary_key=True,default=uuid.uuid4,editable=False)
    task = models.CharField(max_length=200,null=False)
    timestamp = models.DateTimeField(auto_now_add=True,auto_now=False,blank=True)
    completed = models.BooleanField(default=False,null=False)
    updated = models.DateTimeField(auto_now=True,blank=True)
    user = models.ForeignKey(UserModel,on_delete=models.CASCADE,related_name='user',null=False)


