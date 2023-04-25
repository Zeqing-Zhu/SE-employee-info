from django.contrib import admin
from .models import Employee

class EmployeeAdmin(admin.ModelAdmin):
    list_display = ('EmployeeID', 'FirstName', 'LastName', 'EmployeeEmail', 'EmployeePhoneNum', 'AddedDate')
    list_display_links = ('EmployeeID', 'FirstName')
    search_fields = ('EmployeeID', 'FirstName', 'LastName')

    #order by id
    def get_queryset(self, request):
        queryset = super(EmployeeAdmin, self).get_queryset(request)
        queryset = queryset.order_by('EmployeeID')
        return queryset

admin.site.register(Employee, EmployeeAdmin)