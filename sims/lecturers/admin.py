"""include the class models to django admin site"""

from django.contrib import admin
from lecturers.models import (
    Subject as TeacherSubject,
    Score as TeacherScore,
    Attendance as TeachersAttendance,
    Teacher
    )

admin.site.register(TeachersAttendance)
admin.site.register(TeacherScore)
admin.site.register(TeacherSubject)
admin.site.register(Teacher)
