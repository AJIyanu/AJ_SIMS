from django.contrib import admin
"""adds models to admin frontend"""

from .models import Attendance, Student, SubjectReg, Score, ParentStudent, Grade, Guardian

admin.site.register(Attendance)
admin.site.register(Student)
admin.site.register(SubjectReg)
admin.site.register(Score)
admin.site.register(ParentStudent)
admin.site.register(Guardian)
admin.site.register(Grade)
