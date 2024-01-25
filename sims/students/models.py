import uuid
import json
from datetime import date
from django.db import models
from django.core.exceptions import ValidationError
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
    admissionOptions = [('Admitted', 'Admitted'),
                        ('Graduated', 'Graduated'),
                        ('Prospective', 'Prospective')
                        ]
    addmission_status = models.CharField(max_length=15, choices=admissionOptions, default='Prospective')

    def __str__(self) -> str:
        return f"{self.surname} {self.firstname} is registered with admission number: {self.admission_no}"

    def clean(self) -> None:
        """validates phone number
        """
        try:
            int(self.parentphone)
        except ValueError:
            raise ValidationError("Enter a Valid Phone Number")
        if not self.parentphone.startswith('0'):
            raise ValidationError("Enter a Valid Phone Number")

    def save_addmission_no(self, number: str):
        """saves students admission number"""
        self.admission_no = number
        self.save()

class Score(models.Model):
    """creates a score record for the student"""

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    student = models.ForeignKey(Student, on_delete=models.CASCADE, null=False)
    assignment = models.TextField(default=json.dumps([]), editable=False)
    CA_Test = models.TextField(default=json.dumps([]), editable=False)
    exams = models.TextField(default=json.dumps([]), editable=False)
    attendance = models.FloatField(default=0)
    total_score = models.FloatField(default=0, editable=False)
    point = models.FloatField(default=1, editable=False)

    def __str__(self) -> str:
        return f"{self.student.surname} has scored {self.total_score} of 100!"

    def clean(self) -> None:
        """validates assignment
           validates CA_Test
           validates Exams
        """
        try:
            ass = json.loads(self.assignment)
            test = json.loads(self.CA_Test)
            exam = json.loads(self.exams)
        except json.JSONDecodeError:
            raise ValidationError("Not a valid Input")
        for check in [ass, test, exam]:
            if len(check) > 0:
                if "mark obtained" not in check[0]:
                    raise ValidationError("No marks obtained")
                if "mark obtainable" not in check[0]:
                    raise ValidationError("mark obtainable not present")

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

class CourseReg(models.Model):
    """table to register course for the student"""

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    student = models.ForeignKey(Student, on_delete=models.CASCADE, null=False)
    session = models.CharField(max_length=15)
    # course = models.ForeignKey()
    course_code = models.CharField(max_length=10)
    unit = models.IntegerField(default=1)

    def __str__(self) -> str:
        pass
        # course = Course.objects.get(pk=self.course)
        # return f"{course.name} has been registered for {self.session} session"

class Attendance(models.Model):
    """marks attendance for student"""
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    student = models.ForeignKey(Student, on_delete=models.CASCADE, null=False)
    date = models.DateField(default=date.today, null=False)

    def __str__(self) -> str:
        return f"{self.student.surname} {self.student.firstname} is present on {self.date.strftime('%d/%m/%Y')}"



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
