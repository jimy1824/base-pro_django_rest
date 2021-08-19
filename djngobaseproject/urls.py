"""sameditor URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include, re_path
from django.conf import settings
from django.conf.urls.static import static
from rest_framework_jwt.views import verify_jwt_token

from dj_rest_auth.views import LoginView, LogoutView, PasswordResetView, PasswordResetConfirmView
from dj_rest_auth.registration.views import RegisterView, VerifyEmailView, ConfirmEmailView
from rest_framework_simplejwt import views as jwt_views

from accounts.social_auth import FacebookLogin, GoogleLogin

urlpatterns = [
    path('api/register/', RegisterView.as_view()),
    path('api/verify-email/',
         VerifyEmailView.as_view(), name='rest_verify_email'),
    path('api/login/', LoginView.as_view()),
    path('api/token/refresh/', jwt_views.TokenRefreshView.as_view(), name='token_refresh'),
    path(r'api/api-token-verify/', verify_jwt_token),
    path('api/logout/', LogoutView.as_view()),
    path('api/password/reset/', PasswordResetView.as_view(), name='rest_password_reset'),

    path('admin/', admin.site.urls),


    path('api/password/reset/confirm/<uidb64>/<token>/', PasswordResetConfirmView.as_view(),
         name='password_reset_confirm'),




    path('account-confirm-email/<str:key>/', ConfirmEmailView.as_view()),

    # path('api/account-confirm-email/',
    #      VerifyEmailView.as_view(), name='account_email_verification_sent'),
    # re_path(r'^account-confirm-email/(?P<key>[-:\w]+)/$',
    #         VerifyEmailView.as_view(), name='account_confirm_email'),



    path('api/rest-auth/facebook/', FacebookLogin.as_view(), name='fb_login'),
    path('api/rest-auth/google/', GoogleLogin.as_view(), name='google_login'),


    path('accounts/', include('allauth.urls')),

]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
