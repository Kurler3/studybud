from django.shortcuts import render, redirect

from .models import Room

from .forms import RoomForm

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

# WHAT ITEM UPDATING WITH PRIMARY KEY
def updateRoom(request, pk):
    room = Room.objects.get(id=pk)
    
    # PRE-FILL THE FORM WITH THE ROOM DATA
    form = RoomForm(instance=room)
    
    if request.method == "POST":
        # CREATE FORM WITH FILLED DATA, BUT SPECIFY WHICH ROOM TO UPDATE
        form = RoomForm(request.POST, instance=room)
        
        if form.is_valid():
            form.save()
            return redirect('home')
     
    context = {'form': form}
    
    return render(request, 'base/room_form.html', context)

def createRoom(request):

    form = RoomForm()
    
    if request.method == "POST":
        # USE DEFAULT FORM
        form = RoomForm(request.POST)
        # IF DATA PASSED TO FORM IS VALID
        if form.is_valid():
            # SAVE DATA
            form.save()
            
            # IF EVERYTHING WENT OK, REDIRECT TO HOME PAGE
            # CAN JUST PUT THE NAME INSIDE INSTEAD OF THE URL BECAUSE DEFINED IT IN THE urls.py FILE
            return redirect('home')
    
    context = {'form': form}
    
    return render(request, 'base/room_form.html', context)

def deleteRoom(request, pk):
    
    room = Room.objects.get(id=pk)
    
    if request.method == 'POST':
        # DELETE FROM DB
        room.delete()
        
        # REDIRECT TO HOME
        return redirect('home')
        
    context = {'obj': room}
    
    return render(request, 'base/delete.html', context)