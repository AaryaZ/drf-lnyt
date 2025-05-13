from django.contrib import admin
from .models import Student


# Register your models here.
@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'age', 'email','address', 'city')
    # search_fields = ('name',)
    # list_filter = ('age',)
    # ordering = ('-id',)
    # list_per_page = 10
