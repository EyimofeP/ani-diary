from django.urls import path
from django.contrib.auth import views as auth_views #Resetting Password

from . import views

app_name = "author"

urlpatterns = [
	path("auth/register/", views.register, name="register"),
	path("auth/login/", views.signIn, name="login"),
	path("auth/logout/", views.signOut, name="logout"),

	path('auth/reset_password/',auth_views.PasswordResetView.as_view(template_name="author/password_reset.html"),name="reset_password"),
	path('auth/reset_password_sent/',auth_views.PasswordResetDoneView.as_view(template_name="author/password_done.html"), name="password_reset_done"),
	path('auth/reset/<uidb64>/<token>/',auth_views.PasswordResetConfirmView.as_view(template_name="author/password_confirm.html"), name="password_reset_confirm"),
   	path('auth/reset_password_complete/',auth_views.PasswordResetCompleteView.as_view(template_name="author/password_complete.html"), name="password_reset_complete"),

   	path("profile/", views.userAdmin, name="profile"),
]
