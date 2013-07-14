""" side notes:
    SillyContact._meta.get_all_field_names()
    SillyContact._meta.get_field('dob')
    
    https://docs.djangoproject.com/en/dev/ref/contrib/csrf/
    
"""

from django.db import models

# Create your models here.
from django.utils import timezone


class SillyContact(models.Model):
    #
    # TODO - add validators
    #
    first_name = models.CharField(max_length=32)
    last_name = models.CharField(max_length=32)
    dob = models.DateField('date of birth', null=True, default=timezone.now())
    title = models.CharField('job position', max_length=60)
    email = models.EmailField()
    salary = models.DecimalField(null=True, max_digits=18, decimal_places=2)
    
    def __unicode__(self):
        return u'%s %s' % (self.first_name, self.last_name)
        
        
        