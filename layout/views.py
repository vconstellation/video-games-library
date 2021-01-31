from django.shortcuts import render
from django.views.generic import TemplateView, ListView
from django.template.loader import render_to_string
from django.http import JsonResponse
from gamelist.models import GamesCollection
import json

# Create your views here.

def home(request):
    return render(request, 'layout/home.html')

# class SerachResListView(ListView):
#     template_name = 'layout/search_res.html'
#     model = GamesCollection

#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         context["qs_json"] = json.dumps(list(GamesCollection.objects.values()))
#         return context

def search_bar(request):
    url_parameter = request.GET.get('q')

    if url_parameter:
        games = GamesCollection.objects.filter(name__icontains=url_parameter)
    else:
        games = GamesCollection.objects.all()

    if request.is_ajax():
        html = render_to_string(
            template_name='layout/search_res.html',
            context={'context': games}
        )
        
        data_dict = {'html_from_view': html}

        return JsonResponse(data=data_dict, safe=False)

