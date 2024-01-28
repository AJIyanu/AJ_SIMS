"""contains models for lecturers and teachers"""

from uuid import uuid4
from django.db import models
from django.utils import timezone

from schoolAdmin.models import (Classes, Departments, AcademicSession, Term,
                                Subject as AdminSubj, Staff)

class Teacher(models.Model):
    """model class for teacher"""

    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    classes = models.ManyToManyField(Classes, related_name="teachers")
    department = models.ForeignKey(Departments, on_delete=models.SET_NULL, null=True)
    staff = models.OneToOneField(Staff, on_delete=models.CASCADE, default=uuid4)
    subject = models.ManyToManyField("Subject", related_name="teachersubject")

    def __str__(self) -> str:
        return f"Teacher {self.staff.surname} {self.staff.firstname}"


class Subject(models.Model):
    """models class for subject"""

    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    classes = models.ForeignKey(Classes, on_delete=models.CASCADE)
    subject = models.ForeignKey(AdminSubj, on_delete=models.CASCADE)
    name = models.CharField(max_length=20, null=False, editable=False)
    code = models.CharField(max_length=10)
    unit = models.IntegerField(default=1)
    term = models.ManyToManyField(Term, related_name="term_subject")

    def __str__(self) -> str:
        return f"{self.name}, Code: {self.code}"

    def save(self, *args, **kwargs):
        """save overide"""
        self.name = self.subject.name
        super().save(*args, **kwargs)

class Attendance(models.Model):
    """model class for teacher's attendance"""

    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE, null=False)
    teacher = models.ForeignKey(Teacher, on_delete=models.SET_NULL, null=True)
    date = models.DateField(default=timezone.now, null=False)
    session = models.ForeignKey(AcademicSession, on_delete=models.SET_NULL, null=True)
    classes = models.ForeignKey(Classes, on_delete=models.CASCADE)
    term = models.ForeignKey(Term, on_delete=models.SET_NULL, null=True)

    def __str__(self) -> str:
        return f"Attendance for {self.subject.name} on {self.date.strftime('%d/%m/%Y')}"


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
    term = models.ForeignKey(Term, on_delete=models.SET_NULL, null=True)

    def __str__(self) -> str:
        return f"Scoresheet for {self.subject.name}, class {self.classes.name}"
