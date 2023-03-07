from django.db import models

class Blog(models.Model):
    title = models.CharField(max_length=200)
    dataTime = models.DateTimeField()
    discription = models.TextField()
    
    def __str__(self):
        return self.title