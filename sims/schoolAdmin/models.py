"""admin system app for school
"""

from uuid import uuid4
from django.utils import timezone
from django.db import models



class Organogram(models.Model):
    """contains the oreder and hirrachy of staffs"""

    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    position = models.CharField(max_length=20, unique=True)
    level = models.IntegerField()
    description = models.TextField()
    parent_position = models.ForeignKey('self', on_delete=models.SET_NULL, null=True, blank=True)
    is_active = models.BooleanField(default=True)
    createda_at = models.DateField(default=timezone.now, editable=False)

    def __str__(self) -> str:
        return f"{self.position} on level {self.level}"


class Departments(models.Model):
    """describes the different departments in the school"""
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    createda_at = models.DateField(default=timezone.now, editable=False)
    name = models.CharField(max_length=20)
    size = models.IntegerField()

    def __str__(self) -> str:
        return f"{self.name} has a size of {self.size} staffs"


class Classes(models.Model):
    """defines class models for classes offer by the school"""

    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    name = models.CharField(max_length=20)
    size = models.IntegerField()
    createda_at = models.DateField(default=timezone.now, editable=False)

    def __str__(self) -> str:
        return f"{self.name} has a size of {self.size} staffs"


class Subject(models.Model):
    """describes the subjects offered by the school"""
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    name = models.CharField(max_length=15)
    departments = models.ForeignKey(Departments, on_delete=models.SET_NULL, null=True)
    createda_at = models.DateField(default=timezone.now, editable=False)

    def __str__(self) -> str:
        return self.name

class Staff(models.Model):
    """Non teaching staffs for admin system"""

    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    createda_at = models.DateField(default=timezone.now, editable=False)
    organogram = models.ManyToManyField(Organogram, related_name="staff_position")
    surname = models.CharField(max_length=15, null=False)
    firstname = models.CharField(max_length=15, null=False)
    middlename = models.CharField(max_length=15, null=True, blank=True)
    sex_choice = [("Male", "Male"), ("Female", "Female")]
    sex = models.CharField(max_length=8, choices=sex_choice, null=False)
    phonenumber = models.CharField(max_length=15)
    employmentCode = models.CharField(max_length=10, unique=True)
    address = models.TextField()

    def __str__(self) -> str:
        return f"{self.surname} has been employed as\
            {', '.join(obj.position for obj in self.organogram.prefetch_related('staff_position'))}"

class AcademicSession(models.Model):
    """table to track academic session"""

    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    createda_at = models.DateField(default=timezone.now, editable=False)
    start_date = models.DateField(default=timezone.now)
    end_date = models.DateField(default=timezone.now)
    description = models.CharField(max_length=15)
    remarks = models.TextField()

    def __str__(self) -> str:
        return f"Starts {self.start_date.strftime('%m/%Y')} and ends {self.end_date.strftime('%m/%Y')}"


class Term(models.Model):
    """session break down"""

    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    name_choice = [("First", "First"), ("Second", "Second"), ("Third", "Third")]
    name = models.CharField(max_length=10, choices=name_choice, default="First")
    starts = models.DateField(default=timezone.now)
    ends = models.DateField(default=timezone.now)
    session = models.ForeignKey(AcademicSession, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return f"{self.name} starts: {self.starts.strftime('%m/%Y')}, ends: {self.ends.strftime('%m/%Y')}"
