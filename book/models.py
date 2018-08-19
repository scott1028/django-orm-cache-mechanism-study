# Create your models here.
from django.db import models
from django.utils.functional import cached_property

# add to settings.INSTALLED_APPS if you have model in this app of django project.
# Default table name in database will be ${App_Name}_${Class_Name} of this django project
class Storage(models.Model):
    label = models.CharField(max_length=30)
    description = models.CharField(max_length=100)

    # Ref: https://docs.djangoproject.com/en/2.1/ref/utils/#django.utils.functional.cached_property
    # https://stackoverflow.com/questions/15645559/django-typeerror-int-object-is-not-callable
    # This work like QuerySet cache, it will use cached data when the secondary invoking of this method of same instance or pointer 
    # >> for o in qs: print(o.detail)
    @cached_property  # Note!! this is a property, not a method!!
    def detail(self):
        print('[Computing start]')
        val = [100]
        val.append(50)
        print('[Computing end]')
        return val

    def no_cached_detail(self):
        print('[Computing start]')
        val = 100
        val += 10
        print('[Computing end]')
        return val
