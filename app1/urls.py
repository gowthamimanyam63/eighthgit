from django.urls import path
from app1.views import *
app1_name='anything1'
urlpatterns=[
    path('string1/',string1,name='string1'),
    path('string2/',string2,name='string2'),
]