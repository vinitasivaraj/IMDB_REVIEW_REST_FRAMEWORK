from django.db import models
from django.core.validators import MaxValueValidator,MinValueValidator
from django.contrib.auth.models import User

class StreamPlatform(models.Model):
    name=models.CharField(max_length=30)
    about= models.CharField(max_length=150)
    website= models.URLField(max_length=100)

    def __str__(self):
        return self.name
# Create your models here.
class Watchlist(models.Model):
    title=models.CharField(max_length=255)
    storyline= models.CharField(max_length=200)
    platform=models.ForeignKey(StreamPlatform, related_name='watchlist', on_delete=models.CASCADE,default=None)
    avg_rating = models.FloatField(default=0)
    number_rating=models.IntegerField(default=0)
    active = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.title
    
class Review(models.Model):
    review_user=models.ForeignKey(User,on_delete=models.CASCADE)
    rating=models.PositiveBigIntegerField(validators=[MinValueValidator(1),MaxValueValidator(5)])
    description=models.CharField(max_length=255,null=True)
    watchlist=models.ForeignKey(Watchlist,on_delete=models.CASCADE,related_name='reviews')
    active=models.BooleanField(default=True)
    created =models.DateTimeField(auto_now_add=True)
    update=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.rating) +"_"+ self.watchlist.title