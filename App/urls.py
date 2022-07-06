from django.urls import path
from .import views

urlpatterns = [
    path('',views.index,name='index'),
    path('signup/',views.create_profile,name="signup"),
    path('login/',views.Login,name="Login"),
    path('profile/',views.profile,name="pr"),

]
