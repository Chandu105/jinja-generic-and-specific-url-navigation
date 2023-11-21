from specific.views import *
from django.urls import path
app_name='specific'
urlpatterns=[
    path('chandu/',chandu,name='chandu'),
    path('mouni/',mouni,name='mouni'),
]