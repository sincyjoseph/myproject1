from django.db import models


# Create your models here.

class UserDetailsModel(models.Model):
    id = models.AutoField(primary_key=True)
    fname = models.CharField(max_length=255, default='NULL')
    lname = models.CharField(max_length=255, default='NULL')
    mname = models.CharField(max_length=255, default='NULL')
    datepicker = models.DateField(max_length=10)
    email = models.EmailField(max_length=255)

    GENDER_CHOICES = (
        ('M', 'Male'),
        ('F', 'Female'),
    )

    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
    country = models.CharField(max_length=255)
    state = models.CharField(max_length=255)
    file = models.FileField(upload_to='media/', default=0)
    objects = models.Manager()
