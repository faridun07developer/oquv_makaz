from django.urls import path
from .views import (SubjectListAPI, SubjectCreateAPI, PupilsListAPI,
                    PupilsCreateAPI, TeacherCreateAPI, TeacherListAPI,
                    RoomCreateAPI, RoomListAPI)


urlpatterns = [
    path('subject_list/', SubjectListAPI.as_view()),
    path('subject_create/', SubjectCreateAPI.as_view()),
    path('pupils_list/', PupilsListAPI.as_view()),
    path('pupils_create/', PupilsCreateAPI.as_view()),
    path('teacher_create/', TeacherCreateAPI.as_view()),
    path('teacher_list/', TeacherListAPI.as_view()),
    path('room_create/', RoomCreateAPI.as_view()),
    path('room_list/', RoomListAPI.as_view())
]

