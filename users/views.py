from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from .models import Profile
from .forms import ProfileUpdateForm, ProfileGameCollectionUpdate

# Create your views here.

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('layout-home')
    else:
        form = UserCreationForm()
    return render(request, 'users/register.html', {'form': form})

@login_required
def profile(request):
    return render(request, 'users/profile.html')


@login_required()
def profile_update(request):
    if request.method == 'POST':
        form = ProfileUpdateForm(request.POST,
                                 request.FILES,
                                 instance=request.user.profile)
        if form.is_valid():
            temp_save = form.save(commit=False)
            checkbox = form.cleaned_data['platform_checkbox']
            temp_save.platform_used = str(checkbox)
            temp_save.save()
            return redirect('profile')

    else:
        form = ProfileUpdateForm(instance=request.user.profile)

    context = form
    return render(request, 'users/profile_update.html', {'context': context})

@login_required()
def profile_game_collection_update(request):
    if request.method == 'POST':
        form = ProfileGameCollectionUpdate(request.POST, instance=request.user.profile)
        if form.is_valid():
            form.save()
            return redirect('profile')

    else:
        form = ProfileGameCollectionUpdate(instance=request.user.profile)

    context = form
    return render(request, 'users/profile_game_update.html', {'context': context})
