from django.urls import path
from . import views

urlpatterns = [
    path("login/", views.sign_in, name="login"),
    path("register/", views.sign_up, name="register"),
    path("logout/", views.logout_view, name="logout"),
    path("me/", views.profile_view, name="profile"),
    path("me/edit/", views.edit_profile, name="edit_profile"),
]
