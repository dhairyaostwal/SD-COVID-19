from django.urls import path
from . import views

urlpatterns = [
    path('',views.home),
    path('services/',views.services),
    path('about/',views.about),
]
