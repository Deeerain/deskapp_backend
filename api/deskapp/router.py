from rest_framework.routers import DefaultRouter

from api.deskapp import viewsets


router = DefaultRouter()

router.register('apps', viewsets.AppViewset)
