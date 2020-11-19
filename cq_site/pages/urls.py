from django.urls import path

from . import views

urlpatterns = [
    path('', views.home_view),
    path('register', views.reg_view),
    path('login', views.log_view),
    path('logout', views.logoutUser, name="logout"),
    path('thread/<int:id>', views.thread_view),
    path('user/<int:id>', views.user_view),
    path('newthread', views.thread_creation_view)
]