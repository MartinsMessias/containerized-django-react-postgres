from django.urls import path, include
from rest_framework.routers import DefaultRouter

from . import views

api_router = DefaultRouter()
api_router.register(r'users', views.UserViewSet)
api_router.register(r'groups', views.GroupViewSet)

urlpatterns = [
    path('api-auth', include('rest_framework.urls', namespace='rest_framework')),
    path('api/', include(api_router.urls)),
    path('', views.index, name='index')
]
