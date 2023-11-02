from django.urls import path
from .views import SignUpView

from django.contrib.auth.views import (
    PasswordResetView,
    PasswordResetDoneView,
    PasswordResetConfirmView,
    PasswordResetCompleteView,
)

urlpatterns = [
    path('signup/', SignUpView.as_view(), name='signup'),
    path('password-reset/done/', PasswordResetDoneView.as_view(template_name = 'registration/passResetDone.html'), name='password_reset_done'),
    path('password-reset/', PasswordResetView.as_view(template_name = 'registration/passReset.html'), name='password-reset'),
    path('password_reset/confirm/<uidb64>/<token>/', PasswordResetConfirmView.as_view(template_name = 'registration/passResetConfirm.html'), name='password_reset_confirm'),
    path('password_reset/complete/', PasswordResetCompleteView.as_view(template_name = 'registration/passResetComplete.html'), name='password_reset_complete'),
]