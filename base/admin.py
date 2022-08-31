from django.contrib import admin

# Register your models here.

from .models import Message, Room, Topic

# REGISTERING THE ROOM TABLE 
admin.site.register(Room)

# REGISTERING TOPIC
admin.site.register(Topic)

# REGISTERING MESSAGE
admin.site.register(Message)