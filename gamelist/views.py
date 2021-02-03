from django.shortcuts import render, redirect, get_object_or_404
from .forms import GamesCollectionForm, GamesCollectionAddForm
from .models import GamesCollection
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import DetailView, View, TemplateView
from django.views.generic.edit import FormMixin
from django.urls import reverse
from django.http import JsonResponse

def create_game(request):
    if request.method == 'POST':
        form = GamesCollectionForm(request.POST, request.FILES)
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
    model = GamesCollection

class GamesCollectionDetailView(LoginRequiredMixin, FormMixin, DetailView):
    model = GamesCollection
    form_class = GamesCollectionAddForm

    
    def get_success_url(self):
        return reverse('game-detail', kwargs={'pk': self.object.id})

    #Form used to update profile's games collection
    def get_context_data(self, **kwargs):
        context = super(GamesCollectionDetailView, self).get_context_data(**kwargs)
        context['form'] = GamesCollectionAddForm(initial={'games_collection_id': self.object})
        return context

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        user = request.user.profile
        form = self.get_form()
        print(form)
        if form.is_valid():
            print(form)
            obj = form.save(commit=False)
            obj.games_collection_id = self.object.pk
            obj.profile_id = request.user.profile.pk
            obj.save()
            return super(GamesCollectionDetailView, self).form_valid(form)
        



class GamesCollectionJsonListView(View):

    def get(self, *args, **kwargs):
        upper = kwargs.get('num_games')
        lower = upper - 8
        games = list(GamesCollection.objects.values()[lower:upper])
        games_list_size = len(GamesCollection.objects.all())
        max_size = True if upper >= games_list_size else False
    
        
        return JsonResponse({'data': games, 'max': max_size}, safe=False)