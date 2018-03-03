from django.db import models

# Create your models here.



class Employee(models.Model):

    username = models.CharField(max_length=50)
    email = models.EmailField(unique=True)
    address = models.CharField(max_length=255)
    city = models.CharField(max_length=50)
    picture = models.FileField(upload_to='static/images/')


    def __str__(self):

        return self.username


class Employee1(models.Model):

    name = models.CharField(max_length=50)
    email = models.EmailField(unique=True)
    address = models.CharField(max_length=255)




class User(models.Model):

    username = models.CharField(max_length=100)
    email = models.EmailField()


    class Meta:

        db_table = 'users'

class Profile(models.Model):

    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    address = models.TextField()
    created_at = models.DateTimeField()
    city = models.CharField(max_length=100)


    class Meta:

        db_table = 'profile'
























class Student(models.Model):

    emp_id = models.ForeignKey(Employee, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    email = models.EmailField()

