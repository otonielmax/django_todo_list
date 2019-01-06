from django.db import models

# Create your models here.
class Todo(models.Model):
    description = models.CharField(max_length=100)
    status = models.BooleanField(default=False)

    def __str__(self):
        return self.description
