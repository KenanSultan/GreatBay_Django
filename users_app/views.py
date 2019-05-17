from django.shortcuts import render, redirect
from .forms import CustomerCreateForm
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy

def logout_view(request):
    logout(request)
    return redirect('login')

@login_required(login_url=reverse_lazy('login'))
def homepage(request):

    # logout(request)

    return render(request, 'homepage.html')

def login_view(request):
    if request.user.is_authenticated:
        return redirect('homepage')

    if request.method == 'POST':
        username = request.POST.get('username', '')
        password = request.POST.get('password', '')

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('homepage')

    return render(request, 'login.html')

def registration(request):

    if request.method == 'POST':
        m = CustomerCreateForm(request.POST)
        if m.is_valid():
            m.save()
            request.session['username'] = request.POST.get('username')
            return redirect('login')
        else:
            return render(request, 'registration.html', context={
                'registration_form': m
            })

    context = {
        'registration_form': CustomerCreateForm()
    }

    return render(request, 'registration.html', context=context)