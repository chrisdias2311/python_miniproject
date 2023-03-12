from django.db import models

# Create your models here.
# Create your Database here.


class Contact(models.Model):
    name = models.CharField(max_length=25)
    email = models.EmailField()
    phonenumber = models.CharField(max_length=12)
    decription = models.TextField()

    def __str__(self):
        return self.email


class Enroll(models.Model):
    Fullname = models.CharField(max_length=25)
    Email = models.EmailField()
    Gender = models.CharField(max_length=12)
    PhoneNumber = models.CharField(max_length=12)
    DOB = models.CharField(max_length=50)
    SelectMembershipplan = models.CharField(max_length=200)
    SelectTrainer = models.CharField(max_length=55)
    Referenec = models.CharField(max_length=55)
    Address = models.TextField()
    paymentStatus = models.CharField(max_length=55, blank=True, null=True)
    price = models.IntegerField(max_length=55, blank=True, null=True)
    DueDate = models.DateTimeField(blank=True, null=True)
    timeStamp = models.DateTimeField(auto_now_add=True, blank=True)

    def __str__(self):
        return self.Fullname


class Trainer(models.Model):

    name = models.CharField(max_length=55)
    gender = models.CharField(max_length=12)
    phone = models.CharField(max_length=12)
    salary = models.IntegerField(max_length=25)
    timeStamp = models.DateTimeField(auto_now_add=True, blank=True)

    def __str__(self):
        return self.name


class MembershipPlan(models.Model):
    plan = models.CharField(max_length=185)
    price = models.IntegerField(max_length=55)

    def __int__(self):
        return self.id
