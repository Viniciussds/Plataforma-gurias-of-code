from django.urls import path
from . import views as users_views
urlpatterns = [
    # nome, fução que carrega views. 
    path('login/',users_views.loginPage ,name="login"),
    path('singup/',users_views.singUp ,name="singup"),
    
]
