from django.db import models

# Create your models here.
class Branch(models.Model):
    branch=models.CharField(max_length=60, primary_key=True)
class Schemes(models.Model):
    scheme=models.CharField(max_length=10,primary_key=True)
    st_year=models.IntegerField()
    end_year=models.IntegerField()
    branches=models.ManyToManyField(Branch)

    def __str__(self):
        return self.scheme
class Subjects(models.Model):
    course_code=models.CharField(max_length=10,primary_key=True)
    subject=models.CharField(max_length=50)
    category=models.CharField(max_length=6)
    scheme=models.ManyToManyField(Schemes)
    semester=models.IntegerField()
    branch = models.ManyToManyField(Branch)
    mode=models.CharField(max_length=10)
    credits=models.DecimalField(max_digits=10, decimal_places=2)
    type=models.CharField(max_length=10)
    end_exam_marks=models.IntegerField()
    cia_marks=models.IntegerField()
    total_marks=models.IntegerField()
    def __str__(self):
        return self.subject

class Faculty(models.Model):
    faculty_id = models.CharField(primary_key=True, max_length=10)
    faculty_name = models.CharField(max_length=50)

class Faculty_Mapping(models.Model):
    faculty_id=models.ForeignKey(Faculty, on_delete=models.CASCADE)
    branch=models.ForeignKey(Branch, on_delete=models.CASCADE)
    semester=models.IntegerField()
    section=models.CharField(max_length=1)
    course_code=models.ForeignKey(Subjects, on_delete=models.CASCADE)
class Comprehensive(models.Model):
    roll_no=models.CharField(max_length=10, primary_key=True)
    branch=models.ForeignKey(Branch, on_delete=models.CASCADE)
    semester=models.IntegerField()
    section=models.CharField(max_length=1)
    current_scheme=models.ForeignKey(Schemes, on_delete=models.CASCADE)
    cgpa=models.DecimalField(max_digits=5, decimal_places=2)
    total_credits=models.DecimalField(max_digits=10, decimal_places=2)
    is_active = models.BooleanField(default=True)
    is_detained = models.BooleanField(default=False)
    is_gap = models.BooleanField(default=False)
    def __str__(self):
        return self.roll_no
class Gpa(models.Model):
    roll_no=models.ForeignKey(Comprehensive, on_delete=models.CASCADE)
    semester=models.IntegerField()
    gpa=models.DecimalField(max_digits=5, decimal_places=2)
class Detention(models.Model):
    roll_no = models.ForeignKey(Comprehensive, on_delete=models.CASCADE)
    finished_sem = models.IntegerField()
    last_scheme = models.ForeignKey(Schemes, on_delete=models.CASCADE)
    dtype = models.CharField(max_length=15)
    dyear = models.IntegerField()
    attendance_percentage = models.DecimalField(max_digits=5,decimal_places=2)
    reason = models.TextField()
    doc_proof = models.FileField(upload_to='documents/')

class Marks(models.Model):
    roll_no=models.ForeignKey(Comprehensive, on_delete=models.CASCADE)
    semester=models.IntegerField()
    course_code=models.ForeignKey(Subjects, on_delete=models.CASCADE)
    cia_marks=models.IntegerField()
    end_exam_marks=models.IntegerField()
    total_marks=models.IntegerField()
    has_backlog= models.BooleanField(default=True)
    credits=models.DecimalField(max_digits=6, decimal_places=1)

class Inactive(models.Model):
    roll_no=models.ForeignKey(Comprehensive, on_delete=models.CASCADE)
    inactive_type=models.CharField(max_length=9)
    year=models.IntegerField()
    drop_reason=models.TextField(null=True)
    gap=models.IntegerField(default=0)
    gap_reason=models.TextField(null=True)