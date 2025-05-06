from django.urls import path, include
from rest_framework.routers import DefaultRouter
from student.api.views import StudentViewSet

router = DefaultRouter()
router.register(r'student', StudentViewSet)

urlpatterns = [
    path('api/v1/', include(router.urls)),
]