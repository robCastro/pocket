from django.contrib import admin
from expenses import models
# Register your models here.

admin.site.register(models.Category)
admin.site.register(models.Expense)