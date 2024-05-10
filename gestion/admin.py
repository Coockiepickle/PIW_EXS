from django.contrib import admin

from .models import Restaurants, Commentaires, TypeResto

# Register your models here.

admin.site.register(Restaurants)
admin.site.register(Commentaires)
admin.site.register(TypeResto)