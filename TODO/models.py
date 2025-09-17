from django.db import models

# Create your models here.
class TODO(models.Model):
    need_to = models.CharField(max_length=20)
    #created_on = models.TimeField(auto_now=False, auto_now_add=True)


