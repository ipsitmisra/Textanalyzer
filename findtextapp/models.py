from django.db import models

# Create your models here.

class inputtext(models.Model):
    fieldname = models.CharField(max_length = 5000, null=True)
    text = models.TextField(null=True)
    def __str__(self):
        return self.fieldname
