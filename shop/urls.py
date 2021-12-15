from django.urls import path
from . import views

urlpatterns = [
    path('shop', views.shop, name='shop'),
    path('<int:product_id>/', views.view_product, name='view_product'),
    path('add/', views.add_product, name="add_product"),
    path('edit/<int:product_id>/', views.edit_product, name='edit_product'),
    path('delete/<int:product_id>/', views.delete_product, name='delete_product'),
    path('add_review/<int:product_id>/', views.add_review, name='add_review'),
]

