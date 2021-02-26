from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.views.generic import TemplateView, UpdateView, DeleteView, DetailView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.urls import reverse_lazy
from .models import Profile, ProfileGamesCollection
from .forms import ProfileUpdateForm, ProfileGameCollectionUpdate, ProfileGameCollectionSingleItemUpdate
    

class ProfileView(LoginRequiredMixin, DetailView):
    model = Profile
    template_name = 'users/profile.html'

class ProfileUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Profile
    form_class = ProfileUpdateForm
    template_name = 'users/profile_update.html'
    
    def get_success_url(self):
        return reverse_lazy('profile', kwargs={'slug': self.object.slug})

    def test_func(self):
        profile = self.get_object()
        if self.request.user == profile.user:
            return  True
        return False

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
def profile_game_collection_update(request):
    if request.method == 'POST':
        form = ProfileGameCollectionUpdate(request.POST, instance=request.user.profile)
        if form.is_valid():
            obj =  request.user.profile

            game_obj = form.cleaned_data['games_collection']
            playing = form.cleaned_data['currently_playing']
            finished_obj = form.cleaned_data['finished']

            if obj.profilegamescollection_set.filter(games_collection=game_obj).exists():
                #todo: raise error here
                pass
            else:                        
                game_coll_save_obj = ProfileGamesCollection(profile=obj, games_collection=game_obj, currently_playing=playing, finished=finished_obj)
                game_coll_save_obj.save()


            return redirect('profile', slug=request.user.profile.slug)

    else:
        form = ProfileGameCollectionUpdate(instance=request.user.profile)

    context = form
    return render(request, 'users/profile_game_update.html', {'context': context})

@login_required
def profile_game_collection_remove(request, pk, slug):
    user_profile = request.user.profile
    game = user_profile.profilegamescollection_set.get(pk=pk)
    if slug == user_profile.slug:
        game.delete()
        return redirect('profile', slug=request.user.profile.slug)

@login_required
def profile_single_game_update(request, pk, slug):
    user_profile = request.user.profile
    game = user_profile.profilegamescollection_set.get(pk=pk)
    if slug == user_profile.slug:
        if request.method == 'POST':
            form = ProfileGameCollectionSingleItemUpdate(request.POST, instance=user_profile)
            if form.is_valid():
                playing = form.cleaned_data['currently_playing']
                finished_obj = form.cleaned_data['finished']
                game_obj = game.games_collection

                ProfileGamesCollection.objects.filter(pk=game.pk).update(currently_playing=playing)
                ProfileGamesCollection.objects.filter(pk=game.pk).update(finished=finished_obj)
        else:
            form = ProfileGameCollectionSingleItemUpdate(request.POST, instance=user_profile)
                
        context = {'form': form,
                    'game': game}
        

        return render(request, 'users/update_single.html', {'context': context})
        


    
