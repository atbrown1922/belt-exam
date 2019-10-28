from django.db import models

class JobManager(models.Manager):
    def basic_validator(self, postData):
        errors = {}
        # add keys and values to errors dictionary for each invalid field
        if len(postData['title']) < 3:
            errors["title"] = "Job title should be at least 3 characters"
        if len(postData['description']) < 10:
            errors["description"] = "Description should be at least 10 characters"
        return errors

class Job(models.Model):
    title= models.CharField(max_length=65)
    description = models.CharField(max_length=100)
    location = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = JobManager()
    def __repr__(self):
        return f"<Job: {self.title} ({self.description})>"

class UserManager(models.Manager):
    def basic_validator(self, postData):
        errors = {}
        # add keys and values to errors dictionary for each invalid field
        if len(postData['first_name']) < 2:
            errors["first_name"] = "First Name should be at least 2 characters"
        if len(postData['last_name']) < 2:
            errors["last_name"] = "Last Name should be at least 2 characters"
        if len(postData['password']) < 8:
            errors["password"] = "Password should be at least 8 characters"
        return errors

class User(models.Model):
    first_name = models.CharField(max_length=45)
    last_name = models.CharField(max_length=45)
    email = models.TextField()
    password = models.CharField(max_length=45)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = UserManager()
    def __repr__(self):
        return f"<User: {self.first_name} ({self.id}) {self.email}>"



# Create your models here.
