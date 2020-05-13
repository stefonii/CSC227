from django.shortcuts import render

# Create your views here
from django.views import generic
from .models import Fish

# First view:


class FishListView(generic.ListView):
    model = Fish
    template_name = 'fish/fish_list.html'
    context_object_name = 'fishes'
