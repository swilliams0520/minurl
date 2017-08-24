"""minurl URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin

from urls import views

urlpatterns = [
    url(r'^$', views.new_url, name='new_url'),
    url(r'^(?P<slug>[MINURLminurl1vV]{7})$', views.goto_url, name='goto_url'),
    url(r'^c$', views.create_url, name='create_url'),
    url(r'^v/(?P<slug>[MINURLminurl1vV]{7})$', views.view_url, name='view_url'),
]
