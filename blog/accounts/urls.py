from django.urls import path
from . import views


urlpatterns = [
    path('login/', views.login_view.as_view(), name= 'login'),
    path('logout/', views.logout_view, name= 'logout'),
    path('register/', views.register_view.as_view(), name= 'register'),
]