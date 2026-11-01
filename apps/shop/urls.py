from django.urls import path

# from shop.views import home_page_view 

from . import views
#можно так:
#from .views import home_page_view

app_name = 'shop'

urlpatterns = [
    path("", views.home_page_view, name="home_page"),
]