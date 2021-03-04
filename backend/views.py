from django.shortcuts import render
from django.contrib.auth.models import Group, User
from django.shortcuts import render
from django.http import HttpResponse
from rest_framework import viewsets


from backend.serializers import UserSerializer, GroupSerializer
from mysite import settings
import os


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer


class GroupViewSet(viewsets.ModelViewSet):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer


def index(request):
    try:
        with open(os.path.join(settings.REACT_APP_DIR, 'build', 'index.html')) as f:
            return HttpResponse(f.read())
    except FileNotFoundError:
        return HttpResponse(
            """
            Please build the front-end using cd frontend && npm install && npm run
            """,
            status=501,
        )
