"""admin system app for school
"""

from uuid import uuid4
from datetime import date
from django.db import models


class Organogram(models.Model):
    """contains the oreder and hirrachy of staffs"""

    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    position = models.CharField(max_length=20, unique=True)
    level = models.IntegerField()
    description = models.TextField()
    parent_position = models.ForeignKey('self', on_delete=models.SET_NULL, null=True, blank=True)
    is_active = models.BooleanField(default=True)
    createda_at = models.DateField(default=date.today, editable=False)

    def __str__(self) -> str:
        return f"{self.position} on level {self.level}"


class Departments(models.Model):
    """describes the different departments in the school"""
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    createda_at = models.DateField(default=date.today, editable=False)
    name = models.CharField(max_length=20)
    size = models.IntegerField()

    def __str__(self) -> str:
        return f"{self.name} has a size of {self.size} staffs"


class Classes(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    name = models.CharField(max_length=20)
    size = models.IntegerField()
    # teacher = class teacher
    createda_at = models.DateField(default=date.today, editable=False)

    def __str__(self) -> str:
        return f"{self.name} has a size of {self.size} staffs"


class Subject(models.Model):
    """describes the subjects offered by the school"""
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    name = models.CharField(max_length=15)
    departments = models.ForeignKey(Departments, on_delete=models.SET_NULL, null=True)
    createda_at = models.DateField(default=date.today, editable=False)

    def __str__(self) -> str:
        return self.name

class Staff(models.Model):
    """Non teaching staffs for admin system"""

    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    createda_at = models.DateField(default=date.today, editable=False)
    organogram = models.ForeignKey(Organogram, on_delete=models.SET_NULL, null=True)
    surname = models.CharField(max_length=15, null=False)
    surname = models.CharField(max_length=15, null=False)
    middlename = models.CharField(max_length=15, null=False)
    sex_choice = [("Male", "Male"), ("Female", "Female")]
    sex = models.CharField(max_length=8, choices=sex_choice, null=False)
    phonenumber = models.CharField(max_length=15)
    address = models.TextField()

    def __str__(self) -> str:
        return f"{self.surname} has been employed as {self.organogram.position}"
