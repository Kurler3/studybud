from django.urls import path
from . import views

urlpatterns = [
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
