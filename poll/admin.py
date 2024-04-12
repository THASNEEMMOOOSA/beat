from django.contrib import admin
from poll.models import Person
# Register your models here.

class Ppp(admin.ModelAdmin):
    list_display=('id','name','eid','dob','address','email','mobno')

admin.site.register(Person,Ppp)