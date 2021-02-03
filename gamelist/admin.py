from django.contrib import admin
from .models import GamesCollection, Company, GameGenre, GamePlatform

# Register your models here.
admin.site.register(GamesCollection)
admin.site.register(Company)
admin.site.register(GameGenre)
admin.site.register(GamePlatform)