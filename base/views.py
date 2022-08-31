from django.shortcuts import render

from .models import Room

# Create your views here.

# rooms = [
#     {
#         'id': 1,
#         'name': 'Lets learn python!',
#     },
#     {
#         'id': 2,
#         'name': 'Design with me',
#     },
#     {
#         'id': 3,
#         'name': 'Frontend developers',
#     },
# ]


def home(request):
    # GETS ALL ROOMS FROM THE ROOM TABLE
    rooms = Room.objects.all()
    
    context = {'rooms': rooms}
    
    return render(request, 'base/home.html', context)

def room(request, pk):

    room = Room.objects.get(id=int(pk))
     
    context = {'room': room}
    
    return render(request, 'base/room.html', context)

def createRoom(request):
    
    return render(request, 'base/room_form.html')