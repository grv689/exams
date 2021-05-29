from django.db import models

class Exam(models.Model):
    ques=models.CharField(max_length=100)
    opt1=models.CharField(max_length=100)
    opt2=models.CharField(max_length=100)
    opt3=models.CharField(max_length=100)
    opt4=models.CharField(max_length=100)
    correct=models.CharField(max_length=100)
