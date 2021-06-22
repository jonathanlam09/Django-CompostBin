from django.conf.urls import url, include
from django.urls import path
from . import views
from createmodels import urls
#from . import callback

urlpatterns = [
    path('', views.homepage),
    path('api/getreadings', views.showreadings),
    path('api/controls', views.control),
]