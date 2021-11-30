from django.urls import path
from . import views

urlpatterns = [
    path('shop', views.shop, name='shop'),
    path('<product_id>', views.view_product, name='view_product'),
]
