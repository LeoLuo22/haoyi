from django.contrib import admin
from .models import HaoyiAccount, HaoyiTransaction, ObjectAccount

# Register your models here.
admin.site.register(HaoyiAccount)
admin.site.register(HaoyiTransaction)
admin.site.register(ObjectAccount)
