from django.views.generic import ListView
from django.views.generic.edit import CreateView
from .models import City


class HomePageView(ListView):
    template_name = "home.html"
    model = City


class NewCapitalView(CreateView):
    template_name = "capital_new.html"
    model = City
    fields = ["city", "country"]
