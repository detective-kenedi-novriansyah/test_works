from django.urls import path, include
from question.views.user import UserModelViewSets
from rest_framework import routers

router = routers.DefaultRouter()
router.register('', UserModelViewSets, basename="user")

urlpatterns = [
    path('', include((router.urls, 'api')))
]