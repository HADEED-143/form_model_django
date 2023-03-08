from django.db import models

# Create your models here.
class PostCv(models.Model):
    designation= (
        ("Manager", "Manager"),
        ("Cashier", "Cashier"),
        ("Operator", "Operator"),
    )

    name = models.CharField(label='Name of Applicant', max_length=50)
    address = models.CharField(label='Address', max_length=100)
    Designation = models.Choices(designation)
    phoneno = models.IntegerField()
    time_submit = models.TimeField()

    def is_valid(self):
        pass

