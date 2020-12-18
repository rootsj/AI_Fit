from django.urls import path
from . import views

app_name = "users"

urlpatterns = [
    path("login", views.login_view, name="login"),
    path("facelogin", views.face_login_view, name="face_login"),
    path("logout", views.logout_view, name="logout"),
    path("forgotpw", views.forgotpw_view, name="forgotpw"),
    path("signup", views.signup_view, name="signup"),
    path("useredit", views.user_edit, name='useredit'),
    path("sports/<str:what_kind>", views.sports_view, name="sports"),
    path("sports/counts/<int:count_result>/<str:what_kind>", views.count_view, name="counts")
]
