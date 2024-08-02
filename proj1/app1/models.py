from django.db import models

# Create your models here.
class Employee(models.Model):
    choice = [('onboarded', "Not onboarded")]
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=100)
    company = models.CharField(null=False,max_length=50)
    email_id = models.EmailField(max_length=50)
    department = models.CharField(null=False,max_length=50)
    dateofJoining = models.DateTimeField()
    status = models.IntegerField(choices=choice)
    projectDomain = models.CharField(max_length=50)
