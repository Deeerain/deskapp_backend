from django.urls import path

from rest_framework_simplejwt import views as simplejwt_views


urlpatterns = [
     path('token/',
          simplejwt_views.TokenObtainPairView.as_view(), name='get_token'),
     path('token/refresh/',
          simplejwt_views.TokenRefreshView.as_view(), name='refresh_token'),
     path('token/verify/',
          simplejwt_views.TokenVerifyView.as_view(), name='token_verify'),
]
