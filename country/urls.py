'''
Created on 23-Jan-2016

@author: minion
'''
from django.conf.urls import url

from . import views


urlpatterns = [
    
    url('get', views.get, name='get'),
]