import uuid
from django.db import models
"""
Contains the model for student registration and attendance
"""


class Student(models.Model):
    """table to collect student information"""

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    surname = models.CharField(max_length=15, null=False)
    firstname = models.CharField(max_length=15, null=False)
    middlename = models.CharField(max_length=15)
    sex_choices = [('Male', 'Male'), ('Female', 'Female')]
    sex = models.CharField(max_length=6, choices=sex_choices, default='Male')
    DateofBirth = models.DateTimeField()
    admission_no = models.CharField(max_length=10, unique=True)
    address = models.TextField()
    parentphone = models.CharField(max_length=15, null=False)

    def __str__(self) -> str:
        return f"{self.surname} {self.firstname}, id_{self.id}"

class Attendance(models.Model):
    """table to track the attendance of the students"""

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    student = models.ForeignKey(Student, on_delete=models.CASCADE, null=False)
    timeDate = models.DateTimeField(null=False)


    def __str__(self) -> str:
        return f"{self.student_id} present on {self.timeDate.strftime()}"
