from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name

class Question(models.Model):
    category = models.ForeignKey(Category, null=True,on_delete=models.CASCADE)
    question = models.CharField(max_length=500)

    def __str__(self):
        return self.question

class Company(models.Model):
    name = models.CharField(max_length=200)
    score = models.IntegerField()
    review = models.TextField()

    def __str__(self):
        return f"{self.name}: {self.score}"
    
class Profile(models.Model):
    user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
    score = models.IntegerField()

    def __str__(self):
        return f"{self.user}: {self.score}"


