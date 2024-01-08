from django.db import models

# Create your models here.
class Subjects(models.Model):
    course_code=models.CharField(max_length=10)
    subject=models.CharField(max_length=50)
    category=models.CharField(max_length=6)
    scheme=models.IntegerField()
    semester=models.CharField(max_length=10)
    type=models.CharField(max_length=10)
    credits=models.DecimalField(max_digits=10, decimal_places=2)
    end_exam_marks=models.IntegerField()
    cia_marks=models.IntegerField()
    total_marks=models.IntegerField()

    def __str__(self):
        return self.subject

class Branch(models.Model):
    branch=models.CharField(max_length=60)
    course_code=models.CharField(max_length=10)

class Faculty_Mapping(models.Model):
    faculty_id=models.CharField(max_length=10)
    branch=models.CharField(max_length=60)
    semester=models.IntegerField()
    section=models.CharField(max_length=1)
    course_code=models.CharField(max_length=10)

class Comprehensive(models.Model):
    roll_no=models.CharField(max_length=10)
    branch=models.CharField(max_length=60)
    semester=models.IntegerField()
    section=models.CharField(max_length=5)
    scheme=models.CharField(max_length=10)
    cgpa=models.DecimalField(max_digits=5, decimal_places=2)
    total_credits=models.DecimalField(max_digits=10, decimal_places=2)
    gpa=models.DecimalField(max_digits=5, decimal_places=2)
    is_active = models.BooleanField(default=True)

class Student_Subject_Mapping(models.Model):
    roll_no=models.CharField(max_length=10)
    course_code=models.CharField(max_length=10)

class Electives(models.Model):
    roll_no=models.CharField(max_length=10)
    semester=models.IntegerField()
    category=models.CharField(max_length=6)
    chosen_subject=models.CharField(max_length=50)

class Detention(models.Model):
    roll_no=models.CharField(max_length=10)
    finished_sem=models.IntegerField()
    last_scheme=models.CharField(max_length=10)
    reason=models.TextField()
    doc_proof = models.FileField(upload_to='documents/')

class Marks(models.Model):
    roll_no=models.CharField(max_length=10)
    semester=models.IntegerField()
    subject=models.CharField(max_length=50)
    cia_marks=models.IntegerField()
    end_exam_marks=models.IntegerField()
    total_marks=models.IntegerField()
    has_backlog= models.BooleanField(default=True)
    credits=models.DecimalField(max_digits=6, decimal_places=1)

class Inactive(models.Model):
    roll_no=models.CharField(max_length=10)
    inactive_type=models.CharField(max_length=9)
    year=models.IntegerField()
    drop_reason=models.TextField(null=True)
    gap_reason=models.TextField(null=True)


class YourModel(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()

    def __str__(self):
        return self.name

    
    


    



