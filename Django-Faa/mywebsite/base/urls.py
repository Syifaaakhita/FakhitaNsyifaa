# blog/urls.py

# from django.urls import home
# from . import views

# urlpatterns = [
# 	path('', views.home)
	
# ]


from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
]