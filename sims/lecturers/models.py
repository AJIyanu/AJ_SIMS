"""contains models for lecturers and teachers"""

from uuid import uuid4
from django.db import models
from django.utils import timezone

from schoolAdmin.models import (Classes, Departments, AcademicSession,
                                Organogram, Subject as AdminSubj)

class Teacher(models.Model):
    """model class for teacher"""

    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    classes = models.ForeignKey(Classes, on_delete=models.SET_NULL, null=True)
    organogram = models.ForeignKey(Organogram, on_delete=models.SET_NULL, null=True)
    department = models.ForeignKey(Departments, on_delete=models.SET_NULL, null=True)
    surname = models.CharField(max_length=15, null=False)
    firstname = models.CharField(max_length=15, null=False)
    middlename = models.CharField(max_length=15)
    sex_choices = [('Male', 'Male'), ('Female', 'Female')]
    sex = models.CharField(max_length=6, choices=sex_choices, default='Male')
    employmentCode = models.CharField(max_length=10, unique=True)
    address = models.TextField()
    phonenumber = models.CharField(max_length=15)



class Subject(models.Model):
    """models class for subject"""

    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    classes = models.ForeignKey(Classes, on_delete=models.CASCADE)
    subject = models.ForeignKey(AdminSubj, on_delete=models.CASCADE)
    name = models.CharField(max_length=20, null=False)
    code = models.CharField(max_length=10)
    unit = models.IntegerField(default=1)
    teacher = models.ForeignKey(Teacher, on_delete=models.SET_NULL, null=True)


class Attendance(models.Model):
    """model class for teacher's attendance"""

    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE, null=False)
    teacher = models.ForeignKey(Teacher, on_delete=models.SET_NULL, null=True)
    date = models.DateField(default=timezone.now, null=False)
    session = models.ForeignKey(AcademicSession, on_delete=models.SET_NULL, null=True)
    classes = models.ForeignKey(Classes, on_delete=models.CASCADE)


class Score(models.Model):
    """models class to define teachers score sheet"""

    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE, null=False)
    classes = models.ForeignKey(Classes, on_delete=models.SET_NULL, null=True)
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE, null=False)
    assignment = models.IntegerField(default=10)
    CA_Test = models.IntegerField(default=20)
    Exam = models.IntegerField(default=60)
    attendance = models.IntegerField(default=10)
    total = models.IntegerField(default=100, editable=False)
    weight = models.IntegerField(default=1)
