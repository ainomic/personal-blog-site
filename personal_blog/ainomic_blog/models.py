from django.db import models

# Create your models here.
class Blog(models.Model):
    title=models.CharField(max_length=100)
    words=models.IntegerField()
    date_created=models.DateTimeField(auto_now_add=True)
    date_updated=models.DateTimeField(auto_now=True)
    desc=models.TextField()

    def __str__(self):
        return self.title    