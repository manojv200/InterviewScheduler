from django.urls import path

from schedules.views import *

urlpatterns = [
        path('register', RegisterView.as_view(), name='register'),
        path('search_user', InterviewView.as_view(), name='search_user'),
    ]