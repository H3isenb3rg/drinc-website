from django.db import models
from django.contrib.auth.models import User
from datetime import date


class Category(models.Model):
    # TODO: valutare se corretto tenere mischiate categorie drink e ingredienti
    #       Magari per i drink valutare tags (Multipli)
    name = models.CharField(max_length=150)

    class Meta:
        verbose_name_plural = "categories"

    def __str__(self):
        return self.name


class Ingredient(models.Model):
    name = models.CharField(max_length=150)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Drink(models.Model):
    name = models.CharField(max_length=150)
    price = models.DecimalField(max_digits=5, decimal_places=2)
    description = models.CharField(max_length=300)  # For string fields better to use empty strings instead of null ones
    ingredients = models.ManyToManyField(Ingredient)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, blank=True, null=True)

    class Meta:
        ordering = ["price"]

    def __str__(self):
        return f"{self.name} - {self.price}€"


class Menu(models.Model):
    name = models.CharField(max_length=150)
    dateL = models.DateField(verbose_name="Date Launch")
    dateC = models.DateField(verbose_name="Date Conclusion", blank=True, null=True)
    drinks = models.ManyToManyField(Drink)

    class Meta:
        ordering = ["dateL"]

    def is_current(self):
        if not self.dateC or self.dateC >= date.today():
            return True
        return False

    def __str__(self):
        return self.name


class Rating(models.Model):
    rating = models.IntegerField()
    notes = models.CharField(max_length=300)
    date = models.DateTimeField(auto_now_add=True, blank=True)
    drink = models.ForeignKey(Drink, on_delete=models.CASCADE)

    class Meta:
        ordering = ["date"]

    def __str__(self):
        return f"[{self.drink.name}] {self.date} - {self.rating}"


# TODO: Voto Compatibilità


# Proxy Class to customize the Django User Model
# https://docs.djangoproject.com/en/dev/topics/auth/customizing/#extending-the-existing-user-model
class Customer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
