from django.urls import path
from app2.views import *
app2_name='anything2'

urlpatterns=[
    path('htmlfile1/',htmlfile1,name='htmlfile1'),
    path('htmlfile2/',htmlfile2,name='htmlfile2'),
]