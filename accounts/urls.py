from django.urls import path
from .views import RegisterView, OTPLoginView

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('login-otp/', OTPLoginView.as_view(), name='login-otp'),
]

