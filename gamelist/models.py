from django.db import models
from django.contrib.auth.models import User
from django.db.models.functions import Coalesce, Round
from django.core.validators import MaxValueValidator, MinValueValidator
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

    #platforms = models.CharField(max_length=8)
    game_platform = models.ManyToManyField(GamePlatform)

    currently_playing = models.BooleanField

    belong_to_company = models.ForeignKey(Company, on_delete=models.CASCADE)
    genre = models.ForeignKey(GameGenre, on_delete=models.CASCADE)

    description = models.TextField(max_length=450, null=True)

    year_released = models.IntegerField(validators=[MaxValueValidator(2021), 
                                                    MinValueValidator(1980)])

    ### Returning average of ratings code block ###

    def rating_avg(self):
        return GamesReviews.objects.filter(game_reviewed=self).aggregate(
                avg=Coalesce(models.Avg('review_score'), 0),
            )['avg']

    def music_rating_avg(self):
        return GamesReviews.objects.filter(game_reviewed=self).aggregate(
                avg=Coalesce(models.Avg('music_score'), 0),
            )['avg']
    
    def story_rating_avg(self):
        return GamesReviews.objects.filter(game_reviewed=self).aggregate(
                avg=Coalesce(models.Avg('story_score'), 0),
            )['avg']

    def visual_rating_avg(self):
        return GamesReviews.objects.filter(game_reviewed=self).aggregate(
                avg=Coalesce(models.Avg('visual_score'), 0),
            )['avg']
        
    def gameplay_rating_avg(self):
        return GamesReviews.objects.filter(game_reviewed=self).aggregate(
                avg=Coalesce(models.Avg('gameplay_score'), 0),
            )['avg']

    ### End of block ###

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

    author = models.ForeignKey(User, on_delete=models.CASCADE)

    review = models.TextField(max_length=600)

    #scale 1 to 5?
    review_score = models.IntegerField()

    music_score = models.IntegerField()
    story_score = models.IntegerField()
    visual_score = models.IntegerField()
    gameplay_score = models.IntegerField()

    def save(self):
        self.review_score = (self.music_score + self.story_score + self.visual_score + self.gameplay_score) / 4
        super(GamesReviews, self).save()


