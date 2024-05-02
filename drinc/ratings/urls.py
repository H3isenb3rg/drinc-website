from django.urls import path

from . import views

app_name = "ratings"
urlpatterns = [
    # ex: /polls/
    path("", views.IndexView.as_view(), name="index"),
    # ex: /drink/5/
    path("<int:pk>/", views.DetailView.as_view(), name="detail"),
    # ex: /drink/5/ratings/
    path("<int:pk>/ratings/", views.RatingsView.as_view(), name="ratings"),
    # ex: /drink/5/vote/
    path("<int:drink_id>/vote/", views.vote, name="vote"),
]
