from rest_framework.routers import DefaultRouter

from api.users import viewsets


router = DefaultRouter()

router.register('users', viewsets.UserViewset)
router.register('positions', viewsets.PositionViewset)
router.register('departments', viewsets.DepartmentViewset)
