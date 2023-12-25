from django.db import models

class User(models.Model):
    id = models.AutoField(primary_key=True)
    email = models.EmailField(unique=True)
    first_name = models.CharField(max_length=30, blank=False)
    last_name = models.CharField(max_length=30, blank=False)
    avatar = models.URLField(blank=False)
    
    class Meta:
        app_label = 'users'