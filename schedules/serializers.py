from rest_framework import serializers

from schedules.models import TblUsers


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = TblUsers
        fields = ['id', 'username', 'email', 'user_type_id', 'user_type', 'start_date', 'end_date']