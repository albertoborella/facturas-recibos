from django.urls import path
from .views import home,register,salir

urlpatterns = [
    # path('', home, name='home'),
    path('register/', register, name='register'),
    path('logout/', salir, name='logout'),
]

