from django.db import models


class Question(models.Model):
    text = models.TextField()

class Answer(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    answer_1 = models.TextField()
    answer_2 = models.TextField()
    answer_3 = models.TextField()
    answer_4 = models.TextField()
