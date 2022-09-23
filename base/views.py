from django.shortcuts import render, redirect
from django.db.models import Q
from .models import Room, Topic
from django.contrib.auth.models import User
from .forms import RoomForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm



# LOGIN PAGE
def loginPage(request):

    page = 'login'
        
    if request.user.is_authenticated:
        return redirect('home')
    
    if request.method == "POST":   
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        # MAKE SURE USER EXISTS
        try:
            user = User.objects.get(username=username)
        except:
            messages.error(request, "User doesn't exist")

        # CHECK IF CREDS ARE CORRECT
        user = authenticate(request, username=username.lower(), password=password)

        # IF CREDS CORRECT
        if user is not None:
            
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, "Wrong credentials")
        
    context = {'page': page}
    
    return render(request, 'base/login_register.html', context)

def registerUser(request):
    page = 'register'

    form = UserCreationForm()
    
    if request.method == "POST":
        # FILL FORM
        form = UserCreationForm(request.POST)

        # CHECK IF IS VALID
        if form.is_valid():
            # SAVING BUT FREEZING IT
            user = form.save(commit=False)
            
            # IF USER CAPITALIZED THEIR USERNAME, MAKE IT LOWERCASE
            user.username = user.username.lower()
            
            # SAVE IT
            user.save()
        
    
    context = {'page': page, 'form': form}
    
    return render(request,'base/login_register.html', context)

def logoutUser(request):
    logout(request)
    return redirect('home')

# Create your views here.
def home(request):

    # GET Q IF EXISTS
    q = request.GET.get('q') if request.GET.get('q') != None else ''
    
    # GETS ALL ROOMS FROM THE ROOM TABLE
    # CHECK IF THE TOPIC NAME OF EACH OBJECT CONTAINS Q (TOPIC NAME IN SEARCH PARAMS)
    # OR IF THE ROOM NAME CONTAINS Q
    rooms = Room.objects.filter(
        Q(topic__name__icontains=q) |
        Q(name__icontains=q) |
        Q(description__icontains=q)
    )
    
    # GET ALL TOPICS
    topics = Topic.objects.all()
    
    context = {'rooms': rooms, 'topics': topics, 'room_count': rooms.count()}
    
    return render(request, 'base/home.html', context)

def room(request, pk):

    room = Room.objects.get(id=int(pk))
     
    context = {'room': room}
    
    return render(request, 'base/room.html', context)


# WHAT ITEM UPDATING WITH PRIMARY KEY
@login_required(login_url="login")
def updateRoom(request, pk):
    room = Room.objects.get(id=pk)
    
    # PRE-FILL THE FORM WITH THE ROOM DATA
    form = RoomForm(instance=room)
    
    if request.user != room.host:
        return HttpResponse("You are not allowed here")
    
    if request.method == "POST":
        # CREATE FORM WITH FILLED DATA, BUT SPECIFY WHICH ROOM TO UPDATE
        form = RoomForm(request.POST, instance=room)
        
        if form.is_valid():
            form.save()
            return redirect('home')
     
    context = {'form': form}
    
    return render(request, 'base/room_form.html', context)

@login_required(login_url="login")
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

@login_required(login_url="login")
def deleteRoom(request, pk):
    
    room = Room.objects.get(id=pk)
    
    if request.user != room.host:
        return HttpResponse("You are not allowed here")
    
    if request.method == 'POST':
        # DELETE FROM DB
        room.delete()
        
        # REDIRECT TO HOME
        return redirect('home')
        
    context = {'obj': room}
    
    return render(request, 'base/delete.html', context)