from django.urls import path

from apps.users.views import UserMeView, UserRegisterView

urlpatterns = [
    path(
        "register/",
        UserRegisterView.as_view(),
        name="user-register"
    ),
    path("me/", UserMeView.as_view(), name="user-me"),
]
