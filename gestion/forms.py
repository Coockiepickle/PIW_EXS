from django import forms
from .models import Commentaires, Restaurants
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class ajoutCommentaireForm(forms.ModelForm):
    class Meta:
        model = Commentaires
        # fields = '__all__'
        exclude = 'userName', 'noRestaurant'

class ajoutRestaurantForm(forms.ModelForm):
    class Meta:
        model = Restaurants
        fields = '__all__'

class modifierRestaurantForm(forms.ModelForm):
    class Meta:
        model = Restaurants
        fields = '__all__'
        
class EnregistrementForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'password1', 'password2']
        
class RechercheForm(forms.Form):
    nom = forms.CharField(max_length=30, required=False)
    ville = forms.CharField(max_length=30, required=False)
    type = forms.CharField(max_length=20, required=False)

class modifierCommentaireForm(forms.ModelForm):
    class Meta:
        model = Commentaires
        fields = '__all__'