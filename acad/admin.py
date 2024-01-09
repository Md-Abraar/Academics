from django.contrib import admin
from acad.models import *

# Register your models here.
admin.site.register(Subjects)
admin.site.register(Branch)
admin.site.register(Comprehensive)
admin.site.register(Student_Subject_Mapping)
admin.site.register(Electives)
admin.site.register(Detention)
admin.site.register(Faculty_Mapping)
admin.site.register(Inactive)
admin.site.register(Marks)
admin.register(Gpa)

