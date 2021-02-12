from django.db import models
from django.contrib.auth.models import User
from PIL import Image

# Create your models here.
class Company(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return (self.name)

class GameGenre(models.Model):
    genre = models.CharField(max_length=20)

    def __str__(self):
        return (self.genre)

class GamePlatform(models.Model):
    game_platform = models.CharField(max_length=16)

    def __str__(self):
        return (self.game_platform)

class GamesCollection(models.Model):
    name = models.CharField(max_length=30)
   # developer = models.CharField(max_length=12)

    cover = models.ImageField(default='default_cover.jpg', upload_to='game_cover')

    #calculated
    score = models.IntegerField

    #platforms = models.CharField(max_length=8)
    game_platform = models.ManyToManyField(GamePlatform)

    currently_playing = models.BooleanField

    belong_to_company = models.ForeignKey(Company, on_delete=models.CASCADE)
    genre = models.ForeignKey(GameGenre, on_delete=models.CASCADE)

    description = models.TextField(max_length=450, null=True)

    def __str__(self):
        return (self.name)

    def save(self):
        super(GamesCollection, self).save()

        img = Image.open(self.cover.path)

        if img.height > 191 or img.width > 264:
            output_size = (191, 264)
            img = Image.open(self.cover.path).resize(output_size)
            img.thumbnail(output_size)
            img.save(self.cover.path)

class GamesReviews(models.Model):

    #ForeignKey, MtO, Many Reviews to each Game
    game_reviewed = models.ForeignKey(GamesCollection, on_delete=models.CASCADE)

    review = models.TextField(max_length=600)

    #scale 1 to 5?
    review_score = models.IntegerField

    #Mayhaps add a detailed scoring - score for music, plot, etc

