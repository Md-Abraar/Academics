from django.urls import path
from . import views

urlpatterns = [
    path("",views.student, name="student"),
    path("inactive",views.inactive, name="inactive"),
    path("detention",views.detention, name="detention"),
    path("student_mapping",views.student_mapping, name="student_mapping"),
    path("faculty_mapping",views.faculty_mapping, name="faculty_mapping"),
    path("electives",views.electives, name="electives"),
    path("subject",views.subject, name="subject"),
    path("marks", views.marks, name="marks")
]