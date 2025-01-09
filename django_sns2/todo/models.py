from django.db import models

# Create your models here.
class TodoModel(models.Model):
    title = models.CharField(max_length=100)
    contents = models.TextField(null=True, blank=True)
    completed = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.title