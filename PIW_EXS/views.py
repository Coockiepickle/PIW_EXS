from django.shortcuts import render, redirect
from gestion.forms import EnregistrementForm, ajoutRestaurantForm, modifierRestaurantForm, ajoutCommentaireForm, RechercheForm, modifierCommentaireForm
from gestion.models import Restaurants, Commentaires
from django.db.models import Q

def accueilView(request):
    return render(request, 'accueil.html')

def aproposView(request):
    return render(request, 'apropos.html')

def restaurantsView(request):
    restaurants = Restaurants.objects.all()
    form = RechercheForm()
    if request.method == 'POST':
        form = RechercheForm(request.POST)
        if form.is_valid():
            query = Q()
            if form.cleaned_data['nom']:
                query &= Q(nomRestaurant__icontains=form.cleaned_data['nom'])
            if form.cleaned_data['ville']:
                query &= Q(villeRestaurant__icontains=form.cleaned_data['ville'])
            if form.cleaned_data['type']:
                query &= Q(typeRestaurant__nomType__icontains=form.cleaned_data['type'])
            restaurants = Restaurants.objects.filter(query)
    return render(request, 'restaurants.html', {'Restaurants': restaurants, 'form': form})

def connexion(request):
    return render(request, 'connexion.html')

def enregistrement(request):
    form = EnregistrementForm()
    if request.method == 'POST':
        form = EnregistrementForm(request.POST)
        if form.is_valid():
            form.save()
    return render(request, 'enregistrement.html', {'form': form})

def ajoutRestaurant(request):
    form = ajoutRestaurantForm()
    if request.method == 'POST':
        form = ajoutRestaurantForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('restaurants')
    return render(request, 'ajoutRestaurant.html', {'form': form})

def SelectmodifierRestaurant(request):
    form = modifierRestaurantForm()
    restaurants = Restaurants.objects.all()
    if request.method == 'POST':
        restaurant = Restaurants.objects.get(noRestaurant=request.POST['nomRestaurant'])
        return redirect('modifierRestaurant', restaurant.noRestaurant)
    return render(request, 'SelectmodifierRestaurant.html', {'form': form, 'Restaurants': restaurants})

def modifierRestaurant(request, pk):
    restaurant = Restaurants.objects.get(noRestaurant=pk)
    form = modifierRestaurantForm(instance=restaurant)
    if request.method == 'POST':
        form = modifierRestaurantForm(request.POST, instance=restaurant)
        if form.is_valid():
            form.save()
            return redirect('restaurants')
    return render(request, 'modifierRestaurant.html', {'form': form})

def supprimerRestaurant(request):
    restaurants = Restaurants.objects.all()
    if request.method == 'POST':
        Restaurants.objects.filter(noRestaurant=request.POST['nomRestaurant']).delete()
    return render(request, 'supprimerRestaurant.html', {'Restaurants': restaurants})

def detailRestaurant(request, pk):
    restaurant = Restaurants.objects.get(noRestaurant=pk)
    return render(request, 'detailRestaurant.html', {'Restaurant': Restaurants.objects.get(noRestaurant=restaurant.noRestaurant)})

def ajoutCommentaire(request, pk):
    form = ajoutCommentaireForm()
    restaurant = Restaurants.objects.get(noRestaurant=pk)
    if request.method == 'POST':
        form = ajoutCommentaireForm(request.POST)
        if form.is_valid():
            commentaire = form.save(commit=False)
            commentaire.userName_id = request.user.id
            commentaire.noRestaurant_id = restaurant.noRestaurant
            commentaire.save()
            return redirect('detailRestaurant', restaurant.noRestaurant)
    return render(request, 'ajoutCommentaire.html', {'form': form,'Commentaires': commentaires, 'Restaurant': restaurant})

def commentaires(request, pk):
    restaurant = Restaurants.objects.get(noRestaurant=pk)
    commentaires = Commentaires.objects.filter(noRestaurant=restaurant.noRestaurant)
    return render(request, 'commentaires.html', {'Commentaires': commentaires, 'Restaurant': restaurant})

def gestion(request):
    commentaires = Commentaires.objects.filter(userName=request.user)
    return render(request, 'gestion.html', {'Commentaires': commentaires})

def modifierCommentaire(request, pk):
    commentaire = Commentaires.objects.get(noCommentaire=pk)
    if request.method=="POST":
        form = modifierCommentaireForm(request.POST, instance=commentaire)
        if form.is_valid():
            form.save()
            return redirect('detailRestaurant', commentaire.noRestaurant_id)
    else:
        form = modifierCommentaireForm(instance=commentaire)
    return render(request,'modifierCommentaire.html', {'form':form, 'Commentaires':commentaires})    

def supprimerCommentaire(request,pk):
    commentaire = Commentaires.objects.get(noCommentaire=pk)
    if request.method == 'POST':
        commentaire.delete()        
        return redirect('detailRestaurant', commentaire.noRestaurant_id) 
    return render(request,'supprimerCommentaire.html',{'Commentaires':commentaires}) 
