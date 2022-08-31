from django.db import models

# USER MODEL
from django.contrib.auth.models import User

# Create your models here.


# TOPIC TABLE
class Topic(models.Model):
    
    #NAME OF TOPIC
    name = models.CharField(max_length=200)
    
    def __str__(self):
        return self.name

# ROOM TABLE
class Room(models.Model):
    host = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    
    # IF A TOPIC IS DELETED, SET ROOM TO NULL
    topic = models.ForeignKey(Topic, on_delete=models.SET_NULL, null=True)
    
    # ROOM NAME
    name = models.CharField(max_length=200)

    # DESCRIPTION (SAME AS CHAR FIELD JUST BIGGER)
    # BY DEFAULT, WILL BE NULL
    # BLANK = TRUE MEANS THIS FIELD CAN BE SAVED AS AN EMPTY STRING
    description = models.TextField(null=True, blank=True)
    
    # USERS ACTIVE IN THE ROOM
    # participants 

    # ANYTIME AN ITEM FROM THIS TABLE IS UPDATED, SETS THE VALUE TO THE TIME IT IS BEING UPDATED.
    updated = models.DateTimeField(auto_now=True)
    
    # WHEN IT WAS CREATED
    # AUTO NOW ADD MEANS WHEN IT WAS ADDED, SO NO SNAPSHOTS LATER ON, IT WILL NEVER CHANGE
    created = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.name
    
    
# MESSAGE MODEL
class Message(models.Model):
    
    # GOING TO USE THE DEFAULT DJANGO USER TABLE
    # if the user is deleted, also delete the message
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    
    # ONE TO MANY RELATIONSHIP (ONE ROOM CAN HAVE MANY MESSAGES)
    # IF ROOM IS DELETE, DELETE THE MESSAGE (THATS WHAT CASCADE DOES)
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    
    body = models.TextField()
    
    # ANYTIME AN ITEM FROM THIS TABLE IS UPDATED, SETS THE VALUE TO THE TIME IT IS BEING UPDATED.
    updated = models.DateTimeField(auto_now=True)
    
    # WHEN IT WAS CREATED
    # AUTO NOW ADD MEANS WHEN IT WAS ADDED, SO NO SNAPSHOTS LATER ON, IT WILL NEVER CHANGE
    created = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.body[0:50]