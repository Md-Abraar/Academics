from django.urls import path
from . import views
#app_name = 'acad'
urlpatterns = [
    path("",views.student, name="student"),
    path("inactive",views.inactive, name="inactive"),
    path("detention",views.detention, name="detention"),
    path("student_mapping",views.student_mapping, name="student_mapping"),
    path("faculty_mapping",views.faculty_mapping, name="faculty_mapping"),
    path("electives",views.electives, name="electives"),
    path("subject",views.subject, name="subject"),
    path("marks", views.marks, name="marks"),
    path('show', views.show, name='show'),
    path('delete/<int:record_id>/', views.delete_record, name='delete_record'),
    path('edit/<int:record_id>/', views.edit_record, name='edit_record')
]