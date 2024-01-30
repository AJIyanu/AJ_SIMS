"""registers models to django admin"""

from django.contrib import admin
from .models import Staff, Organogram, Subject, Classes, Departments, AcademicSession, Term
from django.contrib.auth.models import Permission

admin.site.register(Staff)
admin.site.register(Organogram)
admin.site.register(Subject)
admin.site.register(Classes)
admin.site.register(Departments)
admin.site.register(AcademicSession)
admin.site.register(Term)
admin.site.register(Permission)
