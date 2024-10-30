from .serializer import PupilsSerializer, TeacherSerializer, SubjectSerializer, RoomSerializer
from .models import Room, Teacher, Subject, Pupils
from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.views import APIView
from django.shortcuts import get_object_or_404
from decimal import Decimal
from datetime import timedelta, datetime


# Create your views here.
# --------------------------------subject start--------------------------------
class SubjectListAPI(generics.ListAPIView):
    queryset = Subject.objects.all()
    serializer_class = SubjectSerializer


class SubjectCreateAPI(APIView):

    def post(self, request):
        data = request.data
        subject_time_str = data.get('subject_time')  # Vaqtni qator sifatida olish
        juftmi = data.get('juftmi')  # Juft kunlar yoki toq kunlar uchun ma'lumot olish

        # Qatorni datetime formatiga aylantirish
        try:
            subject_time = datetime.strptime(subject_time_str, '%Y-%m-%dT%H:%M:%S')  # ISO formatini o‘qish
        except ValueError:
            return Response({"error": "Vaqt noto'g'ri formatda kiritilgan."}, status=status.HTTP_400_BAD_REQUEST)

        # Boshlanish vaqti va tugash vaqti (2 soat keyin)
        subject_time_end = subject_time + timedelta(hours=2)

        # Hafta kunini aniqlash (0 = Dushanba, 6 = Yakshanba)
        hafta_kuni = subject_time.weekday()

        # Yakshanba kuni dars qo'yish mumkin emas
        if hafta_kuni == 6:
            return Response({"error": "Yakshanba dam olish kuni. Dars qo'yish mumkin emas."},
                            status=status.HTTP_400_BAD_REQUEST)

        # Juftmi to'g'ri tekshirish
        if juftmi:  # Agar toq kunlarda bo'lsa (Dushanba, Chorshanba, Juma)
            if hafta_kuni not in [0, 2, 4]:  # Toq kunlar
                return Response({"error": "Dars faqat Dushanba, Chorshanba, va Juma kunlari bo'lishi mumkin."},
                                status=status.HTTP_400_BAD_REQUEST)
        else:  # Agar juft kunlarda bo'lsa (Seshanba, Payshanba, Shanba)
            if hafta_kuni not in [1, 3, 5]:  # Juft kunlar
                return Response({"error": "Dars faqat Seshanba, Payshanba, va Shanba kunlari bo'lishi mumkin."},
                                status=status.HTTP_400_BAD_REQUEST)

        # Boshlanish va tugash vaqt oralig'ida dars band yoki yo'qligini tekshirish
        if Subject.objects.filter(
                subject_time__lte=subject_time_end,  # 2 soat oralig'ida dars bo'lsa
                subject_time__gte=subject_time  # Boshlanish vaqti bu oralig'da bo'lsa
        ).exists():
            return Response({"error": "Bu vaqt oralig'ida boshqa dars band."}, status=status.HTTP_400_BAD_REQUEST)

        # Agar vaqt oralig'i bo'sh bo'lsa, serializer orqali darsni saqlash
        serializer = SubjectSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response({"status": "Yangi predmet qo'shildi", "data": serializer.data},
                            status=status.HTTP_201_CREATED)

        # Validatsiya xatolarini qaytarish
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
# --------------------------------subject end--------------------------------


# --------------------------------teacher start--------------------------------
class TeacherListAPI(generics.ListAPIView):
    queryset = Teacher.objects.all()
    serializer_class = TeacherSerializer


class TeacherCreateAPI(generics.CreateAPIView):
    queryset = Teacher.objects.all()
    serializer_class = TeacherSerializer
# --------------------------------teacher end--------------------------------


# --------------------------------Room start--------------------------------
class RoomListAPI(generics.ListAPIView):
    queryset = Room.objects.all()
    serializer_class = RoomSerializer


class RoomCreateAPI(generics.CreateAPIView):
    queryset = Room.objects.all()
    serializer_class = RoomSerializer
# --------------------------------Room end --------------------------------


# --------------------------------Pupils start--------------------------------
class PupilsListAPI(generics.ListAPIView):
    queryset = Pupils.objects.all()
    serializer_class = PupilsSerializer


class PupilsCreateAPI(APIView):
    def post(self, request):
        data = request.data
        serializer = PupilsSerializer(data=data)
        if serializer.is_valid():
            pupils = serializer.save()

            subject = pupils.subject
            kursNarxi = subject.kurs_price
            teacher = subject.teacher
            soni = teacher.number_of_students
            soni += 1
            salary = (soni * kursNarxi) * (teacher.percent) / 100
            # teacher.salary += (Decimal(teacher.percent) / Decimal(100))   # Maoshni oshirish
            teacher.salary = salary
            teacher.number_of_students = soni
            teacher.save()
            print(subject)
            print(teacher)
            print(teacher.salary)

            # salary = teacher.salary
            # percent = teacher.percent

            data = {
                "status": "Malumot sqalandi",
                "data": serializer.data
            }
            return Response(data)
        else:
            data = {
                "status": "Malumot yaroqli emas"
            }
            return Response(data)
# --------------------------------Pupils end--------------------------------

