
"""
Contains the model for student registration and attendance
"""
import uuid
import json
import sys
from django.utils import timezone
from django.db import models
from django.core.exceptions import ValidationError

sys.path.append("../")

from lecturers.models import (
    Score as TeacherScore,
    Attendance as TeacherAttendance,
    Subject as TeacherSubject,
    )
from schoolAdmin.models import Classes, AcademicSession, Term


class Guardian(models.Model):
    """creates a model for students parent"""

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title = models.CharField(max_length=10)
    surname = models.CharField(max_length=15, null=False)
    firstname = models.CharField(max_length=15, null=False)
    middlename = models.CharField(max_length=15, null=True, blank=True)
    sex_choices = [('Male', 'Male'), ('Female', 'Female')]
    sex = models.CharField(max_length=6, choices=sex_choices, default='Male')
    address = models.TextField()
    phone = models.CharField(max_length=15, null=False)

    def __str__(self) -> str:
        return f" welcome {self.title} {self.surname}"


class Student(models.Model):
    """table to collect student information"""

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    passport = models.ImageField(null=True, blank=True)
    guardian = models.ManyToManyField(Guardian, through="ParentStudent")
    surname = models.CharField(max_length=15, null=False)
    firstname = models.CharField(max_length=15, null=False)
    middlename = models.CharField(max_length=15, null=True, blank=True)
    sex_choices = [('Male', 'Male'), ('Female', 'Female')]
    sex = models.CharField(max_length=6, choices=sex_choices, default='Male')
    DateofBirth = models.DateField()
    admission_no = models.CharField(max_length=10, unique=True)
    address = models.TextField()
    phone = models.CharField(max_length=15, null=True, blank=True)
    admissionOptions = [('Admitted', 'Admitted'),
                        ('Graduated', 'Graduated'),
                        ('Prospective', 'Prospective')
                        ]
    addmission_status = models.CharField(max_length=15, choices=admissionOptions, default='Prospective')

    def __str__(self) -> str:
        return f"{self.surname} {self.firstname} is registered with admission number: {self.admission_no}"


    def save_addmission_no(self, number: str):
        """saves students admission number"""
        self.admission_no = number
        self.save()


class ParentStudent(models.Model):
    """a join table for relationship between Guardian and Students"""

    guardians = models.ForeignKey(Guardian, on_delete=models.CASCADE)
    students = models.ForeignKey(Student, on_delete=models.CASCADE)
    relationship = models.CharField(max_length=15)
    is_master = models.BooleanField(default=False)
    is_sponsor = models.BooleanField(default=False)

    def __str__(self) -> str:
        return f"{self.guardians.title} {self.guardians.surname} is a guardian to {self.students.surname} {self.students.firstname}"


class SubjectReg(models.Model):
    """table to register course for the student"""

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    student = models.ForeignKey(Student, on_delete=models.CASCADE, null=False)
    session = models.ForeignKey(AcademicSession, on_delete=models.CASCADE)
    subject = models.ManyToManyField(TeacherSubject, related_name="students")
    classes = models.ForeignKey(Classes, on_delete=models.SET_NULL, null=True)

    def __str__(self) -> str:
        return f"\
            {'. '.join(obj.name for obj in self.subject.prefetch_related('students'))} \
                has been registered by {self.student.surname} for {self.session.description} session"


class Score(models.Model):
    """creates a score record for the student"""

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    student = models.ForeignKey(Student, on_delete=models.CASCADE, null=False)
    score = models.ForeignKey(TeacherScore, on_delete=models.CASCADE, null=False)
    assignment = models.JSONField(default=list, editable=False)
    CA_Test = models.JSONField(default=list, editable=False)
    exams = models.JSONField(default=list, editable=False)
    attendance = models.FloatField(default=0)
    total_score = models.FloatField(default=0, editable=False)
    point = models.FloatField(default=1, editable=False)
    session = models.ForeignKey(AcademicSession, on_delete=models.SET_NULL, null=True)

    def __str__(self) -> str:
        return f"{self.student.surname} has scored {self.total_score} of 100!"

    def setScore(self, score, mkobt, mkobtnbl):
        """sets mark for student"""
        score_set = {"ass": self.assignment, "test": self.CA_Test, "exam": self.exams}
        if score not in score_set:
            return
        scoreToset = score_set.get(score)
        scoreObj: list = json.loads(scoreToset)
        scoreObj.append({"mark obtained": mkobt, "mark obtainable": mkobtnbl})
        scoreToset = json.dumps(scoreObj)
        if score == "ass":
            self.assignment = scoreToset
        elif score == "test":
            self.CA_Test = scoreToset
        elif score == "exam":
            self.exams = scoreToset
        self.calScore()
        self.save()

    def calScore(self, score=None):
        """calculates the total score of the student"""
        ass = json.loads(self.assignment)
        ass = calcScore(10, ass)
        test = calcScore(20, json.loads(self.CA_Test))
        exam = calcScore(60, json.loads(self.exams))
        score_set = {"ass": ass, "test": test, "exam": exam}
        self.total_score = ass + test + exam + self.attendance
        if score is None or score not in score_set:
            return self.total_score
        return score_set.get(score)

class Attendance(models.Model):
    """marks attendance for student"""
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    attendance = models.ForeignKey(TeacherAttendance, on_delete=models.CASCADE, null=False)
    student = models.ForeignKey(Student, on_delete=models.CASCADE, null=False)
    date = models.DateField(default=timezone.now)

    def __str__(self) -> str:
        return f"{self.student.surname} {self.student.firstname} is present on {self.date.strftime('%d/%m/%Y')}"

    def save(self, *args, **kwargs) -> None:
        """ensure that date carries the teacher's attendance date"""
        self.date = self.attendance.date
        return super().save(*args, **kwargs)


class Grade(models.Model):
    """total grade of a student"""

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    student = models.ForeignKey(Student, on_delete=models.CASCADE, null=False)
    classes = models.ForeignKey(Classes, on_delete=models.SET_NULL, null=True)
    session = models.ForeignKey(AcademicSession, on_delete=models.CASCADE)
    gradePercent = models.FloatField(editable=False, default=0)
    gradeCGPA = models.FloatField(editable=False, default=1)
    gradeAlpha = models.CharField(max_length=2, editable=False, default="F")
    teacherRemarks = models.TextField()
    principalRemarks = models.TextField()
    is_available = models.BooleanField(default=False)
    term = models.ForeignKey(Term, on_delete=models.SET_NULL, null=True)

    def __str__(self) -> str:
        return f"{self.student.surname} overall grade is {self.gradePercent}% ({self.gradeAlpha})"

def calcScore(maxScore, scores: dict={}):
    """returns the total score out of max score"""
    mkobtanble = 0
    mkobtnd = 0
    for marks in scores:
        mkobtanble += marks.get("mark obtainable", 0)
        mkobtnd += marks.get("mark obtained", 0)
    try:
        return mkobtnd / mkobtanble * maxScore
    except ZeroDivisionError:
        print(scores)
        return 0
