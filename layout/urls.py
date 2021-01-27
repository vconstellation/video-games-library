from django.urls import path
from . import views
from users import views as user_views
from gamelist import views as game_views
from django.contrib.auth.urls import views as auth_views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('', views.home, name='layout-home'),
    path('register/', user_views.register, name='register'),
    path('login/', auth_views.LoginView.as_view(template_name='users/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='users/logout.html'), name='logout'),
    path('profile/<slug:slug>', user_views.ProfileView.as_view(), name='profile'),
    path('profile_update/', user_views.profile_update, name='profile-update'),
    path('game_collection_update/', user_views.profile_game_collection_update, name='profile-game-update'),
    path('profile/<slug:slug>/delete/<int:pk>/', user_views.profile_game_collection_remove, name='profile-game-delete'),
    path('games/create/', game_views.create_game, name='create-game'),
    path('games/list/', game_views.GamesCollectionListView.as_view(template_name='gamelist/games-list.html'), name='games-list'),
    path('games/list/<int:num_games>/', game_views.GamesCollectionJsonListView.as_view(), name='games-list'),
    path('games/<int:pk>/', game_views.GamesCollectionDetailView.as_view(), name='game-detail'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
