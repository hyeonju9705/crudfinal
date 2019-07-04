from django.urls import path
from . import views

urlpatterns = [

    path('', views.read, name="home"),
    path('newblog/', views.create, name="newblog"),
    path('update/<int:pk>', views.update, name="update"),
    path('delete/<int:pk>', views.delete, name="delete"),
    path('comment/<int:pk>', views.add_comment, name='add_comment'),
    path('delcomment/<int:pk>', views.del_comment, name='del_comment'),
    path('editcomment/<int:pk>', views.edit_comment, name='edit_comment'),
]