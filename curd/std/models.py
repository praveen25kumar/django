from django.db import models

# Create your models here.


class student(models.Model):
    name = models.CharField(max_length=50)
    email=models.EmailField()
    password=models.CharField(max_length=10)
    createdat=models.DateTimeField(auto_now_add=True)
    mobile=models.IntegerField()


    def __str__(self):
        return self.name



