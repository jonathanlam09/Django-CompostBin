from django.urls import path
from . import views

urlpatterns = [
   path('api/read', views.predict),
   path('ready', views.ready)
]