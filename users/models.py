from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from gamelist.models import GamesCollection, GamesReviews
from django.utils.text import slugify
from PIL import Image
# Create your models here.

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    avatar = models.ImageField(default='default.jpg', upload_to='profile_av')

    slug = models.SlugField(null=True, unique=True)


    nickname = models.CharField(max_length=18)
    bio = models.TextField(max_length=450)

    platform_used = models.CharField(max_length=30)
    #todo: specs (as another model? also completed games)

    #experimental
    review = models.ManyToManyField(GamesReviews)
    game = models.ManyToManyField(GamesCollection, through='ProfileGamesCollection')

    #urls
    steam_link = models.CharField(max_length=20)

    #favorite genre
    #logic that counts how many titles of a certain genre one has in ones collection
    #greatest number dictates what's ones favorite genre

    def save(self, *args, **kwargs):
        self.slug = slugify(self.user.username)
        super(Profile, self).save(*args, **kwargs)

        img = Image.open(self.avatar.path)

        if img.height > 300 or img.width > 300:
            output_size = (300, 300)
            img.thumbnail(output_size)
            img.save(self.avatar.path)

#ManyToMany connecting Profile with GamesCollection

class ProfileGamesCollection(models.Model):
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
    games_collection = models.ForeignKey(GamesCollection, on_delete=models.CASCADE)
    date_joined = models.DateField(default=timezone.now)

    currently_playing = models.BooleanField(null=False, default=False)
    finished = models.BooleanField(null=False, default=False)

