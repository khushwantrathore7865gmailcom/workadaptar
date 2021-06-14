from django.db import models
from month.models import MonthField


# from django import forms
# Create your models here.
class Candidate(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=250)
    email = models.EmailField(max_length=254)
    # password = models.CharField(max_length=32,widget=forms.PasswordInput)
    password = models.CharField(max_length=32)
    created_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.id}-{self.name}"


class Candidate_profile(models.Model):
    user_id = models.ForeignKey(Candidate, on_delete=models.CASCADE, related_name='user')
    birth_day = models.DateField()
    birth_month = MonthField("Month Value", help_text="some help...")
    birth_year = models.IntegerField()
    gender = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    marital_status = models.CharField(max_length=100)
    profile_pic = models.ImageField(upload_to=None)


class Candidate_edu(models.Model):
    user_id = models.ForeignKey(Candidate, on_delete=models.CASCADE, related_name='user_edu')
    institute_id = models.CharField(max_length=250)
    start_date = models.DateField()
    end_date = models.DateField()
    course_type = models.CharField(max_length=250)
    degree = models.CharField(max_length=250)
    created_on = models.DateTimeField(auto_now_add=True)


class Institute(models.Model):
    institute_id = models.IntegerField(primary_key=True)
    institute_name = models.CharField(max_length=250)


class Candidate_profdetail(models.Model):
    user_id = models.ForeignKey(Candidate, on_delete=models.CASCADE, related_name='user_profdetail')
    designation = models.CharField(max_length=250)
    organization = models.CharField(max_length=250)
    salary = models.CharField(max_length=250)
    start_date = models.DateField()
    end_date = models.DateField()


class Candidate_resume(models.Model):
    user_id = models.ForeignKey(Candidate, on_delete=models.CASCADE, related_name='user_resume')
    resume_link = models.FileField()
    coverletter_text = models.CharField(max_length=250)
    coverletter_link = models.FileField()
