from django.db import models


class Teacher(models.Model):
    name = models.CharField(max_length=100)
    surname = models.CharField(max_length=100)
    number_of_students = models.IntegerField()
    salary = models.DecimalField(max_digits=10, decimal_places=2)
    percent = models.IntegerField()

    def __str__(self):
        return f'{self.name} {self.surname}'


class Room(models.Model):
    room_number = models.CharField(max_length=30)

    def __str__(self):
        return self.room_number


# Model Subjects
class Subject(models.Model):
    subject_name = models.CharField(max_length=100)
    teacher = models.ForeignKey('Teacher', on_delete=models.CASCADE)
    subject_room = models.ForeignKey('Room', on_delete=models.CASCADE)
    subject_time = models.DateTimeField()
    juftmi = models.BooleanField(default=True)
    kurs_price = models.IntegerField()

    def __str__(self):
        return self.subject_name


class Pupils(models.Model):
    name = models.CharField(max_length=100)
    surname = models.CharField(max_length=100)
    fathersname = models.CharField(max_length=100)
    subject = models.ForeignKey('subject', on_delete=models.CASCADE)
    password = models.CharField(max_length=16)
    date_of_birth = models.DateField()

    def __str__(self):
        return f'{self.name} {self.surname}'

