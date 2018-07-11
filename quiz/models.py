from django.db import models
from django.contrib.auth.models import User
# Create your models here.
mychoice=(('A','(A)'),('B','(B)'),('C','(C)'),('D','(D)'))
class QuizDetails(models.Model):
    user = models.ForeignKey(User, unique=False)
    question = models.TextField(max_length=100, null=False)
    optionA = models.TextField(max_length=100, null=False)
    optionB = models.TextField(max_length=100, null=False)
    optionC = models.TextField(max_length=100, null=False)
    optionD = models.TextField(max_length=100, null=False)
    correctOption=models.CharField(max_length=1, null=False)
    creationTime = models.DateTimeField(auto_now_add=True)


class ResultLive(models.Model):
    quizId = models.ForeignKey(QuizDetails,unique=False)
    rollNo = models.CharField(max_length=8,null=False)
    response = models.CharField(max_length=1,choices=mychoice,blank=False,default='A')
    responseTime = models.DateTimeField(auto_now_add=True)




