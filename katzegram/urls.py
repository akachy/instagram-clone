from django.urls import path
from . import views

urlpatterns = [
   path('',views.home,name='home'),
   path('login/',views.login_user,name='login'),
   path('logout/',views.logout_user,name='logout'),
   path('register/',views.register,name='register'),
   path('create/',views.create,name='create'),
   path('profile/<int:pk>',views.profile,name='profile'),
]