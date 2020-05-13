from django.shortcuts import render
from django.http import HttpResponseRedirect

from django.views import generic
from .models import Bug
from .forms import CaughtForm


class BugListView(generic.ListView):
    model = Bug
    template_name = 'bug/bug_list.html'
    context_object_name = 'bugs'






