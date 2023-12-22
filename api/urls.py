from django.urls import path, include
from api.deskapp.router import router as deskapp_router
from api.users.router import router as users_router

urlpatterns = [
    path('auth/', include('api.auth.urls')),
    path('', include(deskapp_router.urls)),
    path('', include(users_router.urls)),
]
