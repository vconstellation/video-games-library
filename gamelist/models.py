from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Games_Collection(models.Model):
    name = models.CharField(max_length=20)
    genre = models.CharField(max_length=12)
    developer = models.CharField(max_length=12)

    cover = models.ImageField(default='default_cover.jpg', upload_to='game_cover')

    #calculated
    score = models.IntegerField

    genre = models.CharField(max_length=12)
    platforms = models.CharField(max_length=8)

class Games_Reviews(models.Model):

    #ForeignKey, MtO, Many Reviews to each Game
    game_reviewed = models.ForeignKey(Games_Collection, on_delete=models.CASCADE)

    review = models.TextField(max_length=600)

    #scale 1 to 5?
    review_score = models.IntegerField