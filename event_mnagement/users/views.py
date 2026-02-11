from django.shortcuts import render
from django.shortcuts import render, redirect
from django.contrib.auth import login
from .models import CustomUser
from .forms import CustomUserCreationForm


def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('/')
    else:
        form = CustomUserCreationForm()

    return render(request, 'register.html', {'form': form})

from django.http import HttpResponse


from django.contrib.auth.decorators import login_required

@login_required
def vendor_dashboard(request):
    return HttpResponse("Welcome Vendor")

@login_required
def user_dashboard(request):
    return HttpResponse("Welcome User")
from django.shortcuts import redirect

@login_required
def home(request):
    if request.user.role == 'vendor':
        return redirect('vendor_dashboard')
    elif request.user.role == 'user':
        return redirect('user_dashboard')
    else:
        return redirect('/admin/')

# Create your views here.
