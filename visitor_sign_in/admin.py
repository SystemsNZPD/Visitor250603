from django.contrib import admin
from .models import Form


class FormAdmin(admin.ModelAdmin): #this modeladmin design to create/modify admin interface
    list_display = ("visitor_name", "company_name", "phone_number", "visit_to", "created_at", "sign_out")
    #this class have those "list_display" specific variable , so you should use the exactly name match to "models.py"
    #when django see list_display, it will try to display the column in the (), and the name inside need to corrosped class Form in the models
    search_fields = ("visitor_name", "company_name", "visit_to")
    list_filter = ("visitor_name", "company_name")
    ordering = ("-created_at",)   #- infront of ordering means reverse order
    # readonly_fields = ("occupation",)

admin.site.register(Form, FormAdmin)

"""
go to terminal to create a super user: python manage.py createsuperuser
user: admin, password: Nzpd%13579
"""
