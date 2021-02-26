from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from gamelist.models import GamesCollection
from django.utils.text import slugify
from PIL import Image
# Create your models here.
    
class Platform(models.Model):
    platform = models.CharField(max_length=20)

    def __str__(self):
        return self.platform

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    avatar = models.ImageField(default='default.jpg', upload_to='profile_av')
    background_image = models.ImageField(default='default-bg.jpg', upload_to='profile_bg')

    slug = models.SlugField(null=True, unique=True)


    nickname = models.CharField(max_length=18)
    bio = models.TextField(max_length=450)

    platform_used = models.ManyToManyField(Platform)

    game = models.ManyToManyField(GamesCollection, through='ProfileGamesCollection')

    steam_link = models.CharField(max_length=20, null=True)


    def save(self, *args, **kwargs):
        self.slug = slugify(self.user.username)
        super(Profile, self).save(*args, **kwargs)


        #Resize and save avatar img
        img = Image.open(self.avatar.path)

        if img.height > 300 or img.width > 300:
            output_size = (300, 300)
            img = Image.open(self.avatar.path).resize(output_size)
            img.thumbnail(output_size)
            img.save(self.avatar.path)

        #Resize and save Background img
        bg_img = Image.open(self.background_image.path)

        if bg_img.height > 1920 or bg_img.width > 1080:
            output_size = (1920, 1080)
            bg_img = Image.open(self.background_image.path).resize(output_size)
            bg_img.thumbnail(output_size)
            bg_img.save(self.background_image.path)


    #Methods used to return number of finished and currently playing games
    def calculate_finished_games(self):
        return ProfileGamesCollection.objects.filter(profile=self, finished=True).count()

    def calculate_currently_played_games(self):
        return ProfileGamesCollection.objects.filter(profile=self, currently_playing=True).count()



class ProfileGamesCollection(models.Model):
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
    games_collection = models.ForeignKey(GamesCollection, on_delete=models.CASCADE)
    date_joined = models.DateField(default=timezone.now)

    currently_playing = models.BooleanField(null=False, default=False)
    finished = models.BooleanField(null=False, default=False)





