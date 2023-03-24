from django.db import models


class Form(models.Model):
    """
    Defines the table in the database in which job applicant data is stored.
    Defines columns for:
    - first_name
    - last_name
    - email
    - date_available
    - occupation
    Text fields have a maximum length of MAX_FIELD_LEN
    """
    MAX_FIELD_LEN = 80
    first_name = models.CharField(max_length=MAX_FIELD_LEN)
    last_name = models.CharField(max_length=MAX_FIELD_LEN)
    email = models.EmailField()
    date = models.DateField()
    occupation = models.CharField(max_length=MAX_FIELD_LEN)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
