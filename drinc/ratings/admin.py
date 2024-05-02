from django.contrib import admin

from .models import Drink, Category, Ingredient, Menu, Rating

admin.site.register(Drink)
admin.site.register(Category)
admin.site.register(Ingredient)
admin.site.register(Menu)
admin.site.register(Rating)
