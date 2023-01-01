from django.urls import path
from app.views import *
app_name='prasanna'
urlpatterns=[
    path('operations/',operations,name='operations')
]