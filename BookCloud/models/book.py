from django.db import models
from BookCloud.models.author import Author

class Book(models.Model):
    
    title = models.CharField(max_length=50)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    published_data = models.DateField()
    
    def __str__(self):
        return self.title