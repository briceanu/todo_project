from .models import TodoModel
from .serializers import TodoModelSerializer
from rest_framework import generics,permissions, mixins,viewsets
from .permissions import IsAuthenticatedAndOwner
from rest_framework.response import Response
from rest_framework import status
from rest_framework.exceptions import NotFound
from django.shortcuts import get_object_or_404


# only the Admin can see all the todos
class SeeAllTodosAPI(generics.ListAPIView):
    permission_classes = [permissions.IsAdminUser]
    queryset = TodoModel.objects.all()
    serializer_class = TodoModelSerializer


#  basic CRUD operations
class CreateTodoAPI(generics.GenericAPIView,mixins.CreateModelMixin):
    permission_classes = [permissions.IsAuthenticated]
    queryset = TodoModel.objects.all()
    serializer_class = TodoModelSerializer    

    def post(self,request,*args,**kwargs):
        task = request.data.get('task')
        completed = request.data.get('completed') or False
        if task is None:
            return Response({'error':'no task provided'},status=status.HTTP_400_BAD_REQUEST)
        # extracting the task and user_id from the request
        data = {'task':task,'user':request.user.user_id,'completed': completed}
        # serializing the data
        serializer = self.get_serializer(data=data)
        if serializer.is_valid():
            # if the data is valid save it 
            serializer.save()
            return Response({'todo created': serializer.data}, status=status.HTTP_201_CREATED)
        return Response({'error':serializer.errors},status=status.HTTP_400_BAD_REQUEST)

#  see todos owned by owner
class OwnerTodosAPI(viewsets.GenericViewSet):
    # allowing only the authenticated users to see their todos
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = TodoModelSerializer
    
    def get_queryset(self):
        user_id  = self.request.user.user_id
        try:
            return TodoModel.objects.filter(user_id=user_id)
        except TodoModel.DoesNotExist:
            raise NotFound(detail='No todos found.')

    def list(self,request):
        todos = self.get_queryset() 
        serializer = self.get_serializer(todos,many=True)
        return Response(serializer.data,status=status.HTTP_200_OK)



#  updating a todo owned by owner
# get a task by task_id, if it does not belong to the authenticated user do not update it

class UpdateTodoAPI(generics.GenericAPIView,mixins.UpdateModelMixin):
    # allowing only the authenticated users to see their todos
    permission_classes = [IsAuthenticatedAndOwner]
    serializer_class = TodoModelSerializer

    def get_object(self):
        task_id  = self.request.query_params.get('task_id')
        # if the user_id is not provided throw an error
        if not task_id:
            raise NotFound(detail="task_id query parameter is required")

        try:
            return TodoModel.objects.get(task_id=task_id)
        except TodoModel.DoesNotExist:
            raise NotFound(detail=f'No todo with task_id {task_id} found.')

    
    def put(self,request,*args,**kwargs):
        task = request.data.get('task')
        completed = request.data.get('completed') or False
        if task is None:
            return Response({'error':'no task provided'},status=status.HTTP_400_BAD_REQUEST)
        # extracting the task and user_id from the request
        data = {'task':task,'user':request.user.user_id,'completed': completed}
        
        user_todo = self.get_object()
        # checking the permissions of the client to see if it owns the todo
        self.check_object_permissions(request,user_todo)
        # serializing the data
        serializer = self.get_serializer(user_todo,data=data)
        if serializer.is_valid():
            # if the data is valid save it 
            serializer.save()
            return Response({'todo created': serializer.data}, status=status.HTTP_201_CREATED)
        return Response({'error':serializer.errors},status=status.HTTP_400_BAD_REQUEST)

 

# patch and delete
class UpdateCompleteFieldAPI(viewsets.GenericViewSet):
    queryset = TodoModel.objects.all()
    serializer_class = TodoModelSerializer
    # checking to see if the client is authenticated and owner of the todo
    permission_classes = [IsAuthenticatedAndOwner]

    def partial_update(self,request,pk=None):
        # getting the object to update complete field
        todo = get_object_or_404(self.queryset,pk=pk)

        #  checking to see if the client has permission to modify the object
        self.check_object_permissions(request,todo)
         
        #  if todo_completed is not is the request body throw an error
        todo_completed = request.data.get('completed')
        if todo_completed is None:
            raise NotFound(detail="completed value is required")
        # serializing the data
        data = {'completed':todo_completed}
        serializer = self.get_serializer(todo,data=data,partial=True)
        # checking to see if the data is valid
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_200_OK)
        return Response({'error':serializer.errors},status=status.HTTP_400_BAD_REQUEST)


class RemoveTodoAPI(generics.GenericAPIView,mixins.DestroyModelMixin):
    queryset = TodoModel.objects.all()
    serializer_class = TodoModelSerializer

    def delete(self,request,pk=None,*args,**kwargs):
        # getting te todo to remove
        todo = get_object_or_404(self.queryset,pk=pk)
        # checking the permissions of the todo
        self.check_object_permissions(request,todo)
        # if the client owns the todo and is authenticated we delete the todo
        todo.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
