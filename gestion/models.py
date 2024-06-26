from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator

# Create your models here.

class TypeResto(models.Model):
    noType              = models.AutoField(primary_key=True)
    nomType             = models.CharField(max_length=20)
    def __str__(self):
        return self.nomType

class Restaurants(models.Model):
    noRestaurant        = models.AutoField(primary_key=True)
    nomRestaurant       = models.CharField(max_length=25)
    villeRestaurant     = models.CharField(max_length=25)
    typeRestaurant      = models.ForeignKey(TypeResto,on_delete=models.DO_NOTHING)
    def __str__(self):
        return self.nomRestaurant
    
class Commentaires(models.Model):
    noCommentaire       = models.AutoField(primary_key=True)
    noRestaurant        = models.ForeignKey(Restaurants,on_delete=models.DO_NOTHING)
    userName            = models.ForeignKey(User,on_delete=models.DO_NOTHING)
    commentaire         = models.TextField()   
    note                = models.IntegerField(default=0, validators=[MaxValueValidator(5), MinValueValidator(0)])       
    dateCommentaire     = models.DateField(auto_now_add=True)
    def __str__(self):
        return self.commentaire