from django.db import models
from month.models import MonthField
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager

from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token


# from django import forms
# Create your models here.
class MyAccountManager(BaseUserManager):
    def create_user(self, email, username, password=None):
        if not email:
            raise ValueError('Users must have an email address')
        if not username:
            raise ValueError('Users must have a username')

        user = self.model(
            email=self.normalize_email(email),
            username=username,
        )

        user.set_password(password)
        user.save(using=self._db)
        return user


class Candidate(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=250)
    email = models.EmailField(max_length=254)
    # password = models.CharField(max_length=32,widget=forms.PasswordInput)
    password = models.CharField(max_length=32)
    confirmpass = models.CharField(max_length=32, blank=True)
    created_on = models.DateTimeField(auto_now_add=True)
    is_email_verified = models.BooleanField(default=False)

    objects = MyAccountManager()
    def __str__(self):
        return f"{self.id}-{self.name}"

@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)

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
