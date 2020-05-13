"""acc_site URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include, path

from fish import urls as fish_urls
from bug import urls as bug_urls

from . views import homepage

urlpatterns = [
    path('', homepage),
    path('admin/', admin.site.urls),
    path('fish/', include(fish_urls)),
    path('bug/', include(bug_urls)),

]

admin.site.site_header = 'Animal Crossing Creature Checklist'
admin.site.index_title = 'AC Checklist Administration'
