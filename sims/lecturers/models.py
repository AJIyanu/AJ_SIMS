"""contains models for lecturers and teachers"""

from uuid import uuid4
from datetime import date
from django.db import models


class Teacher(models.Model):
    """model class for teacher"""


    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
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
    name = models.CharField(max_length=20, null=False)
    code = models.CharField(max_length=10)
    unit = models.IntegerField(default=1)
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE, null=False)


class Attendance(models.Model)
    """model class for teacher's attendance"""

    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE, null=False)
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE, null=False)
    date = models.DateField(default=date.today())


class Score(models.Model):
    """models class to define teachers score sheet"""

    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE, null=False)
    # classgrp
    subject = models.ForeignKey(Teacher, on_delete=models.CASCADE, null=False)
    assignment = models.IntegerField(default=10)
    CA_Test = models.IntegerField(default=20)
    Exam = models.IntegerField(default=60)
    attendance = models.IntegerField(default=10)
    total = models.IntegerField(default=100, editable=False)
    weight = models.IntegerField(default=1)
