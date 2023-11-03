from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings



class Question(models.Model):
    text = models.TextField()

class Answer(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    answer_1 = models.TextField()
    answer_2 = models.TextField()
    answer_3 = models.TextField()
    answer_4 = models.TextField()

from django.db import models

class CompanyValue(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    value = models.CharField(max_length=1000)
    created_at = models.DateTimeField(auto_now_add=True)  

class CompanyValueIdea(models.Model):
    company_value = models.ForeignKey(CompanyValue, on_delete=models.CASCADE, related_name='vision_ideas')
    idea = models.TextField()

class PersonValue(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    value=models.CharField(max_length=1000)
    created_at = models.DateTimeField(auto_now_add=True) 

