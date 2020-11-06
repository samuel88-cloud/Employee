from django.db import models

# Create your models here.
class Employee(models.Model):
    CHOICES = (
        ('level 1', 'level 1'),
        ('level 2', 'level 2'),
        ('level 3', 'level 3'),
        ('level 4', 'level 4'),
        ('level 5', 'level 5'),
        ('level 6', 'level 6'),
        ('level 7', 'level 7'),
        ('level 8', 'level 9'),
        ('level 9', 'level 9'),
        ('level 10', 'level 10'),
    )

    salarychoices=(
        ('100.0', '100.0'),
        ('200.0', '200.0'),
        ('300.0', '300.0'),
        ('400.0', '400.0'),
    )

    name=models.CharField(max_length=100,null=True)
    email=models.EmailField()
    age=models.IntegerField()
    salary=models.CharField(max_length=300,choices = salarychoices)
    position = models.CharField(max_length=300, choices = CHOICES)
    address=models.CharField(max_length=500)
    
    

    def __str__(self):
        return f'{self.name}'
    
    class Meta:
        ordering = ['name']

    def get_absolute_url(self):
        return u'/employee/'
