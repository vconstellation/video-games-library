from django.shortcuts import render, redirect
from .forms import GamesCollectionForm
from .models import GamesCollection
from django.views.generic import ListView, DetailView

def create_game(request):
    if request.method == 'POST':
        form = GamesCollectionForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('layout-home')
    else:
        form = GamesCollectionForm()

    return render(request, 'gamelist/create-game.html', {'form': form})

class GamesCollectionListView(ListView):
    model = GamesCollection

class GamesCollectionDetailView(DetailView):
    model = GamesCollection
