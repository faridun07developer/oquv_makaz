from rest_framework import serializers
from .models import Pupils, Teacher, Subject, Room


class PupilsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pupils
        fields = ('name', 'surname', 'fathersname', 'subject', 'password', 'date_of_birth')


class TeacherSerializer(serializers.ModelSerializer):
    class Meta:
        model = Teacher
        fields = ('name', 'surname', 'number_of_students', 'salary', 'percent')


class SubjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subject
        fields = ('subject_name', 'teacher', 'subject_room', 'subject_time', 'juftmi', 'kurs_price')


class RoomSerializer(serializers.ModelSerializer):
    class Meta:
        model = Room
        fields = ('room_number',)

