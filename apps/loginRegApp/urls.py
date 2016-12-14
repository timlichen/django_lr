# APP LEVEL URLS
from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'register$', views.register),
<<<<<<< HEAD
    url(r'login$', views.login)
=======
    url(r'login$', views.login),
    url(r'logout$', views.logout),
    # url(r'register$', views.register),
>>>>>>> 66e2efd558275a9e996b695afa052b8c89cf1701
]
