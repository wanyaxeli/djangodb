from django.shortcuts import render
from rest_framework.views import APIView
from .serializers import UserSerializer
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from .models import User
# Create your views here.
class UserView(APIView):
    permission_classes = [IsAuthenticated]
    def post(self,request):
        data = request.data
        serializer=UserSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)
    def get(self,request):
        user=User.objects.all()
        serializer=UserSerializer(user,many=True)
        return Response(serializer.data)


