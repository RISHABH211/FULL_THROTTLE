from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import user
from .serializers import userSerializers

class userlist(APIView):

    def get(self,request):
        user1=user.objects.all()
        serializer=userSerializers(user1,many=True)
        return Response(serializers.data)
    
    def post(self):
        pass



