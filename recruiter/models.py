from django.db import models
from phone_field import PhoneField
# Create your models here.
class employer(models.Model):
    id = models.IntegerField(primary_key=True)
    name=models.CharField(max_length=250)
    email = models.EmailField(max_length=254)
    phone = PhoneField(blank=True, help_text='Contact phone number')
    company_type=models.CharField(max_length=250)
    company_name = models.CharField(max_length=250)
    # password = models.CharField(max_length=32,widget=forms.PasswordInput)
    password = models.CharField(max_length=32)
    created_on = models.DateTimeField(auto_now_add=True)