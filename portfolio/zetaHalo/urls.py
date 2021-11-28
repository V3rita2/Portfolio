from django.urls import path
from . import views

urlpatterns = [
    #only need one view I think, so lets go, this is the home page
    path('', views.Main.as_view(), name="main"),
]