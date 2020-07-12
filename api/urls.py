from api import views
from django.urls import path, include
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView


urlpatterns = [
    path('user/about', views.GetUserEmail.as_view(), name='userEmail'),
    path('user/register', views.UserRegistration.as_view(), name='userRegistration'),
    path('token/obtain', TokenObtainPairView.as_view(), name='tokenObtain'),
    path('token/refresh', TokenRefreshView.as_view(), name='tokenRefresh'),
]