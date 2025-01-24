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
            user_id =''
            validated_data = serializer.validated_data

            if validated_data['user_type'] == 1:
                validated_data['interviewer_id'] = str(random.randint(10000000, 99999999))
                user_id = validated_data['interviewer_id']
            elif validated_data['user_type'] == 2:
                validated_data['candidate_id'] = str(random.randint(10000000, 99999999))
                user_id = validated_data['candidate_id']

            validated_data['email'] = validated_data['username']

            user = TblUsers.objects.create(**validated_data)
            return Response({"message": "User registered successfully!", "user_id": user_id}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class InterviewView(APIView):
    def post(self, request):
        interviewer_id = request.data.get('interviewer_id')
        candidate_id = request.data.get('candidate_id')
        interviewer = TblUsers.objects.filter(interviewer_id=interviewer_id).first()
        candidate = TblUsers.objects.filter(candidate_id=candidate_id).first()
        if interviewer and candidate:
            min_duration = 1
            times = self.find_common_timeslots(interviewer.start_date, interviewer.end_date, candidate.start_date, candidate.end_date, min_duration)
            response = {'candidate_Name':candidate.first_name+' '+candidate.last_name, 'Interviewer_Name':interviewer.first_name+' '+interviewer.last_name, 'available_timeslots': times}
            return Response(response, status=status.HTTP_200_OK)
        return Response(
            {"error": "User with the given ID does not exist."},
            status=status.HTTP_404_NOT_FOUND,
        )


    def find_common_timeslots(self, slot1_start, slot1_end, slot2_start, slot2_end, min_duration):
        slot1_start = datetime.datetime.fromtimestamp(slot1_start)
        slot1_end = datetime.datetime.fromtimestamp(slot1_end)
        slot2_start = datetime.datetime.fromtimestamp(slot2_start)
        slot2_end = datetime.datetime.fromtimestamp(slot2_end)
        overlap_start = max(slot1_start, slot2_start)
        overlap_end = min(slot1_end, slot2_end)

        min_duration_td = datetime.timedelta(hours=min_duration)
        if overlap_end - overlap_start < min_duration_td:
            return []

        timeslots = []
        current_time = overlap_start
        while current_time + min_duration_td <= overlap_end:
            next_time = current_time + min_duration_td
            timeslots.append(
                f"{current_time.strftime('%Y-%m-%d %I:%M %p')} - {next_time.strftime('%Y-%m-%d %I:%M %p')}")
            current_time = next_time

        return timeslots

