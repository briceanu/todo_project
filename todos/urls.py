from django.urls import path
from . import views
 
 

urlpatterns = [
    path('all_todos',views.SeeAllTodosAPI.as_view(),name='all_todos'),
    path('create_todo',views.CreateTodoAPI.as_view(),name='create_todo'),
    path('owner_todos',views.OwnerTodosAPI.as_view({'get':'list'}),name='owner_todos'),
    path('update_todo',views.UpdateTodoAPI.as_view(),name='update_todo'),
    path('update_complete_field/<uuid:pk>',views.UpdateCompleteFieldAPI.as_view({'patch':'partial_update'}),name='update_complete_field'),
    path('remove_todo/<uuid:pk>',views.RemoveTodoAPI.as_view(),name='remove_todo')
    
    
    ]