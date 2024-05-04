from django.urls import path, include
from . import views as users_views
urlpatterns = [
    path('login/',users_views.loginPage,name='login'),
    path('register/',users_views.register,name='register'),
    path('logout/',users_views.logoutPage,name='logout'),
]
