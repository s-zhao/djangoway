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
        
        
import django_filters  
"""
{% block content %}
    <form action="" method="get">
        {{ filter.form.as_p }}
        <input type="submit" />
    </form>
    {% for obj in filter %}
        {{ obj.name }} - ${{ obj.price }}<br />
    {% endfor %}
{% endblock %}
"""      
class SalariedContact(django_filters.FilterSet):
    
    salary = django_filters.NumberFilter(lookup_type='gt')
    last_name = django_filters.CharFilter(lookup_type='icontains')
    
    class Meta:
        model = SillyContact
        fields = ['salary', 'last_name']
        
        