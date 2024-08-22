from rest_framework.routers import DefaultRouter
from django.urls import path, include
from users.api.views import UserViewSets

router_user = DefaultRouter()
router_user.register(prefix='user', viewset=UserViewSets, basename='user')