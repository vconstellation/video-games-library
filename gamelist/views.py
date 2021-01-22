from django.shortcuts import render, redirect
from .forms import GamesCollectionForm
from .models import GamesCollection
from django.views.generic import DetailView, View, TemplateView
from django.http import JsonResponse

def create_game(request):
    if request.method == 'POST':
        form = GamesCollectionForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('layout-home')
    else:
        form = GamesCollectionForm()

    return render(request, 'gamelist/create-game.html', {'form': form})

# class GamesCollectionListView(ListView):
#     model = GamesCollection
#     paginate_by = 8

class GamesCollectionListView(TemplateView):
    template_name = 'gamelist/games-list.html'

class GamesCollectionDetailView(DetailView):
    model = GamesCollection

class GamesCollectionJsonListView(View):

    def get(self, *args, **kwargs):
        upper = kwargs.get('num_games')
        lower = upper - 8
        games = list(GamesCollection.objects.values()[lower:upper])
        games_list_size = len(GamesCollection.objects.all())
        max_size = True if upper >= games_list_size else False
    
        
        return JsonResponse({'data': games, 'max': max_size}, safe=False)