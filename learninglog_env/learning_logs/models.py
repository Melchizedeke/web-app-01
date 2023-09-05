from django.db import models

# Create your models here.
class Topic(models.Model):
    """A topic the user is learning about"""
    text = models.CharField(max_length=500)
    date_added = models.TimeField(auto_now_add=True)
    
    def __str__(self):
        """Return a string representation of the model."""
        return self.text