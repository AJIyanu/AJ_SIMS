"""registers models to django admin"""

from django.contrib import admin
from .models import Staff, Organogram

admin.site.register(Staff)
admin.site.register(Organogram)
