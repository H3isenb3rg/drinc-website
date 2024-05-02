from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.views import generic

from .models import Drink, Rating


class IndexView(generic.ListView):
    template_name = "ratings/index.html"
    context_object_name = "latest_drink_list"

    def get_queryset(self):
        """Return the last five published questions."""
        return Drink.objects.order_by("-price")[:5]  # TODO: uso date dei menu per prendere i più recenti


class DetailView(generic.DetailView):
    model = Drink
    template_name = "ratings/detail.html"


class RatingsView(generic.DetailView):
    model = Drink
    template_name = "ratings/results.html"


def vote(request, drink_id):
    drink = get_object_or_404(Drink, pk=drink_id)
    try:
        rating = float(request.POST["rating"])
    except (ValueError):
        # Redisplay the question voting form.
        return render(
            request,
            "ratings/detail.html",
            {
                "drink": drink,
                "error_message": "Could not read reating. Retry",
            },
        )
    if rating < 0 or rating > 10:
        return render(
            request,
            "ratings/detail.html",
            {
                "drink": drink,
                "error_message": "Invalid value found in rating. Rating should be between 0 and 10",
            },
        )
    notes = str(request.POST["notes"]).strip()

    rating = Rating(drink_id=drink.id, rating=rating, notes=notes)
    rating.save()
    # Always return an HttpResponseRedirect after successfully dealing
    # with POST data. This prevents data from being posted twice if a
    # user hits the Back button.
    return HttpResponseRedirect(reverse("ratings:ratings", args=(drink.id,)))
