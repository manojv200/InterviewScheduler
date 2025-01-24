from rest_framework import serializers

from schedules.models import TblUsers


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = TblUsers
        fields = ['id', 'username', 'email', 'first_name', 'last_name', 'interviewer_id', 'candidate_id', 'user_type', 'start_date', 'end_date']