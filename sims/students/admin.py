from django.contrib import admin
"""adds models to admin frontend"""

from .models import Attendance, Student, CourseReg, Score

admin.site.register(Attendance)
admin.site.register(Student)
admin.site.register(CourseReg)
admin.site.register(Score)
