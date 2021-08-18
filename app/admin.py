from django.contrib import admin
from .models import UserDetailsModel


class userDetailsAdmin(admin.ModelAdmin):
    list_display = ('id', 'fname', 'lname', 'mname', 'datepicker', 'email', 'gender', 'country', 'state', 'file')


# # Register your models here.
admin.site.register(UserDetailsModel, userDetailsAdmin)
