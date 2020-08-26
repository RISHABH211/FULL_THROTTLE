from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import status
from .models import user,Activity_period
from .serializers import userSerializers,Activity_periodSerializers

class userlist1(viewsets.ModelViewSet):
    
    queryset=user.objects.all()
    serializer_class=userSerializers
class activitylist(viewsets.ModelViewSet):

    queryset=Activity_period.objects.all()
    serializer_class=Activity_periodSerializers
