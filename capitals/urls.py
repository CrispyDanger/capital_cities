from django.urls import path
from .views import HomePageView, NewCapitalView

urlpatterns = [
    path("", HomePageView.as_view(), name="home"),
    path("new/", NewCapitalView.as_view(), name="capital_new"),
]
