from django.db import models

# Create your models here.
from django.db import models

# add to settings.INSTALLED_APPS if you have model in this app of django project.
# Default table name in database will be ${App_Name}_${Class_Name} of this django project
class Storage(models.Model):
    label = models.CharField(max_length=30)
    description = models.CharField(max_length=100)
