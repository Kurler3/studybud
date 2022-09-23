from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.loginPage, name="login"),
    path('register/', views.registerUser, name="register"),
    path('logout/', views.logoutUser, name="logout"),
    # HOME
    path('', views.home, name="home"),
    # ROOM
    path('room/<str:pk>/', views.room, name="room"),
    # CREATE ROOM FORM
    path('create-room', views.createRoom, name="create-room"),
    # UPDATE ROOM FORM
    path('update-room/<str:pk>/', views.updateRoom, name="update-room"),
    # DELETE ROOM
    path('delete-room/<str:pk>/', views.deleteRoom, name="delete-room"),
]
