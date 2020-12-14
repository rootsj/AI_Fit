from django.urls import path
from . import views

app_name = "users"

urlpatterns = [
    path("login", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout"),
    path("signup", views.signup_view, name="signup"),
    path("sports/<str:what_kind>", views.sports_view, name="sports"),       # 추가
]
