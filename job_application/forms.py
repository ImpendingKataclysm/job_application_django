from django import forms
from .models import MAX_FIELD_LEN


class ApplicationForm(forms.Form):
    """
    Collects and stores data entered by the job applicant into the application
    form
    """
    first_name = forms.CharField(max_length=MAX_FIELD_LEN)
    last_name = forms.CharField(max_length=MAX_FIELD_LEN)
    email = forms.EmailField()
    date = forms.DateField()
    occupation = forms.CharField(max_length=MAX_FIELD_LEN)
