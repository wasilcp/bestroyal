
from django.urls import path, include
from . import views 

urlpatterns = [
    path('', views.home),
    path('about',views.home2),
    path('contact',views.home3),
    path('categories',views.categories),
    path('products',views.home5),
    path('single',views.home6)
]
