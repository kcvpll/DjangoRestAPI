from rest_framework import routers
from .api import StudentsViewSet, TeachersViewSet

router = routers.DefaultRouter()
router.register('api/Students', StudentsViewSet, 'Students')
router.register('api/Teachers', TeachersViewSet, 'Teachers')

urlpatterns = router.urls

