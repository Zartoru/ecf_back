from django.db import models

class SchoolYear(models.Model):

    name = models.CharField(max_length=50)
    date_start = models.CharField(max_length=50)
    date_end = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class User(models.Model):

    email = models.CharField(max_length=50)
    roles = models.CharField(max_length=50)
    password = models.CharField(max_length=50)
    firstname = models.CharField(max_length=50)
    lastname = models.CharField(max_length=50)
    phone = models.CharField(max_length=50, null=True)
    school_year_id = models.ForeignKey("SchoolYear", verbose_name=("school_year"), on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.lastname
    
class Project(models.Model):

    name = models.CharField(max_length=50)
    description = models.TextField()
    user_id = models.ManyToManyField("User", verbose_name=("user"))

    def __str__(self):
        return self.name