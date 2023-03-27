from django.contrib import admin
from .models import Form


class FormAdmin(admin.ModelAdmin):
    field_list = ("first_name", "last_name", "email")
    list_display = field_list
    search_fields = field_list
    list_filter = ("date", "occupation")
    ordering = ("first_name", )


admin.site.register(Form, FormAdmin)
