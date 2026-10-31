from django.urls import path

from shop.views import home_page_view 

# from . import views
#можно так:
#from .views import home_page_view



urlpatterns = [
    path("", home_page_view),
]