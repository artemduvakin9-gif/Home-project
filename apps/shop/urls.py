from django.urls import path

# from shop.views import home_page_view 

from . import views
#можно так:
#from .views import home_page_view

app_name = 'shop'

urlpatterns = [
    path("", views.home_page_view, name="home_page"),
    path('product/<int:product_id>/', views.get_product_detail_view, name="product_detail"),
    path('product/add/', views.product_add_view, name='product_add'),
    path('product/<int:product_id>/edit/', views.product_edit_view, name="product_edit"),
]