from django.urls import path
from rest_framework.authtoken.views import obtain_auth_token
from .views import CustomObtainAuthToken

urlpatterns = [
    path('auth/', CustomObtainAuthToken.as_view()),
]