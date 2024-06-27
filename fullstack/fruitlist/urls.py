from django.urls import path
from . import views 
urlpatterns = [
    path('fruitlist/',views.fruits_and_students,name="fruitlist")
]
