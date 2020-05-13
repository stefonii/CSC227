from django.urls import path
from . import views

urlpatterns = [
    path('', views.BugListView.as_view(), name='bug_list'),
]
