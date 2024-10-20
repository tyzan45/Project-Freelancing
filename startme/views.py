from multiprocessing import AuthenticationError
from telnetlib import LOGOUT
from django.shortcuts import redirect, render
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from .forms import ProfileForm
from django.contrib.auth.decorators import login_required
from . decorators import unathenticated_user
from .models import Profile

# Create your views here.
def home(request):
    return render(request, 'index.html') 

#

def index(request):
    # import ipdb; ipdb.set_trace();
    if request.method == "POST":
        username = request.POST.get('username')
        pass1 = request.POST.get('pass1')
        user = authenticate(request, username=username, password=pass1)
        if user is not None:
            login(request,user)
            messages.info(request, 'you are logged in')
            return render(request, 'index.html')    
        else:
            messages.error(request, "Bad Credentials!")
            return render(request, 'index.html')
    else:
        return render(request, 'index.html')



# SIGNUP 
@unathenticated_user
def signupp(request):   
    if request.method == "POST":
        username = request.POST.get('username')
        fname = request.POST.get('fname')
        lname = request.POST.get('lname')
        Email = request.POST.get('Email')
        pass1 = request.POST.get('pass1')
        pass2 = request.POST.get('pass2')
        phone = request.POST.get('phone')
        if pass1!=pass2:
            messages.success(request, "Your password didn't match, please try again")
            return HttpResponse("Your password didnt matched")

        elif User.objects.filter(username=username).exists():
            messages.error(request, 'Sorry, this username is already taken!')
            return render(request, 'signupp.html')

        elif User.objects.filter(email=Email).exists():
            messages.error(request, 'Sorry this email is already taken')
            return render(request, 'signupp.html')

        else:
            myuser = User.objects.create_user(username, Email, pass1)
            myuser.first_name = fname
            myuser.last_name = lname
            myuser.phone = phone
            myuser.save()
            messages.success(request, " Your account has been sucessfully created")
            return render(request, 'index.html')
    else:   
        return render(request, 'signupp.html')


@login_required(login_url='index')
def logout_user(request):
    logout(request)
    messages.info(request, 'You are Logged Out')
    return render(request, 'index.html')

@login_required(login_url='index')                                      
def profile(request):
    if request.method == "POST":
        form = ProfileForm(request.POST, request.FILES, instance=request.user.profile)
        if form.is_valid():
            form.save()
            return redirect('/profile')  # Redirect to avoid form resubmission
        else:
            context = {'form': form}
            return render(request, 'profile.html', context)  # Re-render the profile page with errors if form is invalid
    else:
        form = ProfileForm(instance=request.user.profile)
        context = {'form': form}
        return render(request, 'profile.html', context)


def profilepage(request):
    return render(request, 'profilepage.html') 

def all_users(request):
    users = User.objects.all()
    selected_skill = request.GET.get('dropdown1')
    if selected_skill:
        users = users.filter(profile__desc__icontains=selected_skill)  
    return render(request, 'all_users.html', {'users': users})




@login_required(login_url='index')    
def hehe(request):
    return render(request, 'hehe.html')


def singupp(request):
    return render(request, 'signupp.html')


def hahe(request):
     return render(request, 'hahe.html')

def test2(request):
    return render(request, 'test2.html')

# def my_view(request, username):
#     user = User.objects.get(username=username)
#     profile = user.profile
#     name = profile.name
#     return render(request, 'all_users.html')


# def allfree(request):
#     users = User.objects.all()
#     return render(request, 'allfree.html', {'users': users})


def viewprofile(request,id):
    if id:
        user=User.objects.filter(pk=id).first()
    return render(request,'viewer.html', {'user': user})

def viewer(request):
    return render(request, 'viewer.html')