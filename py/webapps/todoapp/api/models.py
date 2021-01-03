from django.db import models

# Create your models here.


class Task(models.Model):
    """
    Database model for tasks.
    """
    title = models.CharField(max_length=200)
    description = models.CharField(max_length=300, blank=True, null=True)
    completed = models.BooleanField(default=False, blank=True, null=True)
    objects = models.Manager()

    def __str__(self):
        return self.title

