from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect

from .forms import CreateUserForm

from django.contrib.auth.decorators import login_required


# Create your views here.

def loginPage(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('Index')
        else:
            messages.info(request, "Username OR Password is incorrect.")

    return render(request, 'login.html')


def logoutPage(reguest):
    logout(reguest)
    return redirect('Login')


def registerPage(request):
    form = CreateUserForm()

    if request.method == "POST":
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()

            user = form.cleaned_data.get('username')
            messages.success(request, "Account '" + user + "' was created.")
            return redirect("Login")

    contex = {
        'form': form
    }
    return render(request, 'register.html', contex)


@login_required(login_url="Login")
def indexPage(request):
    return render(request, 'index.html')


@login_required(login_url="Login")
def hospitalPage(request):
    return render(request, 'hospital.html')


@login_required(login_url="Login")
def symptomPage(request):
    return render(request, 'symptom.html')
