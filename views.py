from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from .forms import CreateUserForm, LoginUserForm
from django.contrib.auth import authenticate, login, logout
from .models import Question, Profile

# Create your views here.
def home(request):
    return render(request, "home.html")

def about(request):
    return render(request, "about.html")

def loginPage(request):
    form = LoginUserForm

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect("home")

    context = {'form': form}
    return render(request, "login.html", context)

def logoutUser(request):
    if request.user.is_authenticated:
        logout(request)
        return redirect('login')
    else:
        return redirect("home")
    

def signup(request):
    form = CreateUserForm
    questions = Question.objects.all()

    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            score = request.POST.get('score')
            user = form.save()
            newprofile = Profile.objects.create(user=user, score=score)
            newprofile.save()
            return redirect("login")

    context = {'form':form, 'questions':questions}
    return render(request, "signup.html", context)

def profile(request):
    if request.user.is_authenticated:
        return render(request, "profile.html")
    else: 
        return redirect("home")
    
def leaderboard(request):
    profiles = Profile.objects.all()
    context = {"profiles":profiles}
    return render(request, "leaderboard.html", context)

def rewards(request):
    return render(request, "rewards.html")