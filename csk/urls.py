from django.urls import path
from csk.views import *
app_name='everything'
urlpatterns=[
    path('msd/',msd,name='msd'),
]