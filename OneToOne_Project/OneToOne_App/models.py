
# code addedd in local system

from django.db import models

class Student(models.Model):
    sno = models.IntegerField()
    sname = models.CharField(max_length=30)
    marks = models.IntegerField()
    address = models.CharField(max_length=50, default='Hyderabad')

    def __str__(self):
        return self.sname


class Cource(models.Model):
    cno = models.IntegerField()
    cname = models.CharField(max_length=30)
    cfee = models.IntegerField()

    student = models.OneToOneField(Student,on_delete=models.CASCADE)

    def __str__(self):
        return self.cname