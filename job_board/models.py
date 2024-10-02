from django.db import models


# Create your models here.

# model ⇒ python class
# the model represents a table in the db
# attributes are the fields in the table

# job posting table
# title, description, company, salary

class JobPosting(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    company = models.CharField(max_length=100)
    salary = models.IntegerField()
    is_active = models.BooleanField(default=False)

# CRUD
# Create
# Read
# Update
# Delete

# model manager → objects
# JobPosting.objects.all() – returns all objects from the db
# JobPosting.objects.get(id=1) – returns one object from the db
# JobPosting.objects.filter(title="job title) – returns one object from the db
