from django.db import models

class Author(models.Model):
    name = models .CharField(max_length=100)
    identification = models. models.IntegerField()
    birth_day = models. DateField()
    
    def __str__(self):
     return self.name()