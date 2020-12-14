from django.contrib import admin
from django.contrib.auth.models import Group
from .models import User, DailyRecord

# Register your models here.
admin.site.register(User)
admin.site.register(DailyRecord)
admin.site.unregister(Group)
