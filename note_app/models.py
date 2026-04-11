from django.db import models

# Create your models here.

class Note(models.Model):
    title = models.CharField(max_length=200)
    content =models.TextField()
    created_at =models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    # user = models.ForeignKey(user, on_delete=models.CASCADE, related_name='notes')
    def __str__(self):
       return self.title