"""
URL configuration for PIW_EXS project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from PIW_EXS.views import accueilView, aproposView, restaurantsView, connexion, commentaires, enregistrement, detailRestaurant, ajoutRestaurant, SelectmodifierRestaurant, supprimerRestaurant, gestion, modifierRestaurant, ajoutCommentaire, supprimerCommentaire, modifierCommentaire
from django.contrib.auth import views as authentication_views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', accueilView, name='accueil'),
    path('apropos/', aproposView, name='apropos'),
    path('restaurants/', restaurantsView, name='restaurants'),
    path('restaurants/detailRestaurant/<int:pk>/', detailRestaurant, name='detailRestaurant'),
    path('gestion/', gestion, name='gestion'),
    path('gestion/ajout/', ajoutRestaurant, name='ajoutRestaurant'),
    path('gestion/selectmodification/', SelectmodifierRestaurant, name='SelectmodifierRestaurant'),
    path('gestion/modifier/<int:pk>/', modifierRestaurant, name='modifierRestaurant'),
    path('supprimerRestaurant/', supprimerRestaurant, name='supprimerRestaurant'),
    path('restaurants/commentaires/<int:pk>/', commentaires, name='commentaires'),
    path('commentaires/ajout/<int:pk>/', ajoutCommentaire, name='ajoutCommentaire'),
    path('utilisateurs/connexion/', authentication_views.LoginView.as_view(template_name='connexion.html'), name='connexion'),
    path('utilisateurs/enregistrement/', enregistrement, name='enregistrement'),
    path('deconnexion/',authentication_views.LogoutView.as_view(template_name='deconnexion.html'), name='deconnexion'),
    path('commentaires/modif/<int:pk>/', modifierCommentaire, name='modifierCommentaire'),
    path('commentaires/suppr/<int:pk>/', supprimerCommentaire, name='supprimerCommentaire'),
]
