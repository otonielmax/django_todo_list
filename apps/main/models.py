from django.db import models
from django.conf import settings
#from django.contrib.auth.models import User

# Create your models here.
class Todo(models.Model):
    description = models.CharField(max_length=100)
    status = models.BooleanField(default=False)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, default=1, on_delete=models.CASCADE)

    def __str__(self):
        return self.description
