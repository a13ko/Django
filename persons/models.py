from django.db import models

GENDER = (
    ('male' , 'male'),
    ('female' , 'female'),
    ('female' , 'female'),
)

class GenderManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset()
    
    def filter_for_gender(self,gender):
        return self.get_queryset().filter(gender=gender)

# Create your models here.
class Person(models.Model):
    name = models.CharField(max_length=300)
    gender = models.CharField(max_length=300,choices=GENDER)
    age = models.PositiveIntegerField()

    objects = models.Manager()
    types = GenderManager()

    def __str__(self):
        return self.name
    