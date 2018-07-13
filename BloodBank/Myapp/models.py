from django.db import models

class Donor(models.Model):
    BLOOD_CHOICES = (
    ('O+','O+'),
    ('O-', 'O-'),
    ('A+','A+'),
    ('A-','A-'),
    ('B+','B+'),
    ('B-','B-'),
    ('AB+','AB+'),
    ('AB-','AB-'),
)
    GENDER_CHOICES = (
    ('M','Male'),
    ('F', 'Female'),
    ('O','Others'),
)



    First_Name = models.CharField(max_length = 250)
    Last_Name = models.CharField(max_length = 250)
    Email = models.EmailField(max_length=250,unique = True, blank = True)
    Contact_Number = models.IntegerField(unique=True)
    Blood_Group = models.CharField(max_length=6, choices=BLOOD_CHOICES)
    Gender = models.CharField(max_length=6, choices=GENDER_CHOICES)
    Date_of_birth = models.DateField(blank=True)
    Weight = models.IntegerField()
    Address = models.TextField()
    Registered_at = models.DateTimeField(auto_now_add=True, blank = True)

    class Meta:
        verbose_name_plural = "Donor"

    def __str__(self):
        return self.First_Name+ " " + self.Last_Name
class Contact(models.Model):
    Name = models.CharField(max_length = 250)
    Email = models.EmailField(max_length = 250)
    Contact = models.IntegerField()
    Message = models.TextField()
    Date = models.DateTimeField(auto_now_add=True, blank = True)

    class Meta:
        verbose_name_plural = "Contact"

    def __str__(self):
        return self.Name
