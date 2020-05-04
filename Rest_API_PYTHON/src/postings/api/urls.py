from django.urls import path,re_path
#from django.contrib import admin
from.views import ApiPostView, ApiPostCreate






urlpatterns=[
    path('/', ApiPostCreate.as_view(), name='post-create'),
    re_path(r'(?P<pk>\d+)/', ApiPostView.as_view(), name='post'),
    
]