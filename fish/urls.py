from django.urls import path
from . import views

urlpatterns = [
    path('', views.FishListView.as_view(), name='fish_list'),
]
