
from django.urls import path, include
from . import views 

urlpatterns = [
    path('', views.home),
    path('about',views.about),
    path('contact',views.contact),
    path('categories',views.categories),
    path('category/<slug:slug>',views.specific_category),
    path('product/<int:code>',views.product)

    # path('products',views.home5),
]
