from django.db import models

# Create your models here.
class blog(models.Model):
    id = models.AutoField(primary_key=True),
    title=models.CharField(max_length=150)
    words=models.IntegerField()
    date_created=models.DateTimeField(auto_now_add=True)
    date_updated=models.DateTimeField(auto_now_add=True)
    desc=models.TextField()

    def __str__(self):
        return self.title

