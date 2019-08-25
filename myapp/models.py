from django.db import models

# Create your models here.

class gitnoti(models.Model):
	action = models.CharField(max_length=100,null=False)
	repo_name = models.CharField(max_length=100,null=False)
	repo_url = models.CharField(max_length=100)
	sender_name = models.CharField(max_length=100)
	sender_url = models.CharField(max_length=100)