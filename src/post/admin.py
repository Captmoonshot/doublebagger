from django.contrib import admin
from django.db import models

# Register your models here.
from .models import Post, Company

class MyCompanyAdmin(admin.ModelAdmin):
	model = Company
	list_display = ('name', 'slug', 'description', 'pe_ratio',)
	

admin.site.register(Company, MyCompanyAdmin)

