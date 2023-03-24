from django.db import models

MAX_FIELD_LEN = 80


class Form(models.Model):
    """
    Defines the table in the database in which job applicant data is stored.
    Defines columns for:
    - first_name
    - last_name
    - email
    - date_available
    - employment status
    Text fields have a maximum length of MAX_FIELD_LEN
    """
    first_name = models.CharField(max_length=MAX_FIELD_LEN)
    last_name = models.CharField(max_length=MAX_FIELD_LEN)
    email = models.EmailField()
    date = models.DateField()
    employment_status = models.CharField(max_length=MAX_FIELD_LEN)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
