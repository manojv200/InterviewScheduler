import datetime
import random
import uuid

from django.shortcuts import render
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from schedules.models import TblUsers
from schedules.serializers import UserSerializer


# Create your views here.

class RegisterView(APIView):
    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            validated_data = serializer.validated_data

            validated_data['user_type_id'] = str(random.randint(10000000, 99999999))
            validated_data['email'] = validated_data['username']

            user = TblUsers.objects.create(**validated_data)
            return Response({"message": "User registered successfully!", "user_id": user.user_type_id}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class InterviewView(APIView):
    def post(self, request):
        user_id = request.data.get('user_id')
        user = TblUsers.objects.filter(user_type_id=user_id).first()
        if user:
            response = {'Name':user.username, 'start_date': datetime.datetime.fromtimestamp(user.start_date), 'end_date': datetime.datetime.fromtimestamp(user.end_date)}
            return Response(response, status=status.HTTP_200_OK)
        return Response(
            {"error": "User with the given ID does not exist."},
            status=status.HTTP_404_NOT_FOUND,
        )



