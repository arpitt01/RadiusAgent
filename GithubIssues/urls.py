from django.conf.urls import url
from . import views

app_name = "RadiusAgent"
urlpatterns = [
url(r'^$', views.home, name='main'),
url(r'^Results/$', views.results, name='results'),
    ]