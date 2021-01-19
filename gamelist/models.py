from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class GamesCollection(models.Model):
    name = models.CharField(max_length=20)
    genre = models.CharField(max_length=12)
    developer = models.CharField(max_length=12)

    cover = models.ImageField(default='default_cover.jpg', upload_to='game_cover')

    #calculated
    score = models.IntegerField

    genre = models.CharField(max_length=12)
    platforms = models.CharField(max_length=8)

    def __str__(self):
        return (self.name)

class GamesReviews(models.Model):

    #ForeignKey, MtO, Many Reviews to each Game
    game_reviewed = models.ForeignKey(GamesCollection, on_delete=models.CASCADE)

    review = models.TextField(max_length=600)

    #scale 1 to 5?
    review_score = models.IntegerField