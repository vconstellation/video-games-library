from django.shortcuts import render, redirect, get_object_or_404
from .forms import GamesCollectionForm, GamesCollectionAddForm, GamesReviewForm
from .models import GamesCollection, GamesReviews, Company, GameGenre
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import DetailView, View, TemplateView, ListView, CreateView
from django.views.generic.edit import FormMixin
from django.urls import reverse
from django.http import JsonResponse

### Game Collection block ###

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

class GamesCollectionListView(ListView):
    template_name = 'gamelist/games-list.html'
    model = GamesCollection
    paginate_by = 8
    
    

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

### End of Games Collection block ###

### Reviews block ###

class GameReviewCreateView(LoginRequiredMixin, CreateView):
    model = GamesReviews
    template_name = 'gamelist/review_create.html'
    form_class = GamesReviewForm
    

    def get_success_url(self):
        return reverse('game-detail', kwargs={'pk': self.kwargs['pk']})

    #Overriding method in order to pre-populate ForeignKey field [with pk]
    def form_valid(self, form, **kwargs):
        review = form.save(commit=False)
        review.author = self.request.user
        review.game_reviewed_id = self.kwargs['pk']
        #Check if the user has already reviewed the game
        if GamesReviews.objects.filter(game_reviewed_id=self.kwargs['pk'], author=self.request.user):
            pass
        else:
            return super(GameReviewCreateView, self).form_valid(form)
        
class GameReviewListView(ListView):
    model = GamesReviews
    template_name = 'gamelist/review_list.html'

    def get_queryset(self):
        return GamesReviews.objects.filter(game_reviewed=self.kwargs.get('pk'))

class CompanyDetailView(DetailView):
    model = Company
    template_name = 'gamelist/company_detail.html'


