from django.conf.urls import url
from . import views          


urlpatterns = [
    url(r'^$', views.index),
    url(r'^add$', views.add),
    url(r'^reset$', views.reset,)
]



# (?P<num>\d+)  is the variable for any number typed into the URI