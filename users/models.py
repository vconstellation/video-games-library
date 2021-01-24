from django.db import models
from django.contrib.auth.models import User
from gamelist.models import GamesCollection, GamesReviews
from PIL import Image
# Create your models here.

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    avatar = models.ImageField(default='default.jpg', upload_to='profile_av')


    nickname = models.CharField(max_length=18)
    bio = models.TextField(max_length=450)

    #count_of_games = models.IntegerField

    platform_used = models.CharField(max_length=30)
    #todo: specs (as another model? also completed games)

    #experimental
    review = models.ManyToManyField(GamesReviews)
    game = models.ManyToManyField(GamesCollection)

    #urls
    steam_link = models.CharField(max_length=20)

    def save(self, *args, **kwargs):
        super(Profile, self).save(*args, **kwargs)

        img = Image.open(self.avatar.path)

        if img.height > 300 or img.width > 300:
            output_size = (300, 300)
            img.thumbnail(output_size)
            img.save(self.avatar.path)


# class User_Game_Collection(models.Model):
#     user = models.OneToOneField(User, on_delete=models.CASCADE)
#
#     game = models.ManyToManyField(Games_Collection)
#
#
# class User_Game_Reviews(models.Model):
#     user = models.OneToOneField(User, on_delete=models.CASCADE)
#
#     review = models.ManyToManyField(Games_Reviews)
