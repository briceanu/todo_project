from django.urls import path
from . import views


urlpatterns=[
    path('create',views.SignUpAPI.as_view(),name='create_user'),
    path('list',views.ListUsersAPI.as_view(),name='list_users'),
    path('signin',views.SignInAPI.as_view(),name='signin'),
    path('new_access_token',views.NewAccessTokenAPI.as_view(),name='new_access_token'),
    path('logout',views.LogoutAPI.as_view(),name='logout'),
    path('remove_user',views.RemoveUserAPI.as_view(),name='remove_user'),
    path('update_user',views.UpdateUserDataAPI.as_view({'put': 'update'}),name='update_user'),
    path('update_password',views.update_user_password,name='update_password')
    ]