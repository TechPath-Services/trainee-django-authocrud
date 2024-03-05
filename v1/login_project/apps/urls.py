from django.urls import path
from . import views


urlpatterns = [
    path('', views.Index, name="home"),
    path('login/', views.login_view, name='login'),
    path('signup/', views.signup_view, name='signup'),
    path('add/',views.Add_Employee , name='add-employee'),
    
]