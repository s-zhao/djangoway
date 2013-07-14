"""
https://docs.djangoproject.com/en/dev/topics/forms/
https://docs.djangoproject.com/en/dev/ref/forms/fields/


    first_name = models.CharField(max_length=32)
    last_name = models.CharField(max_length=32)
    dob = models.DateTimeField('date of birth', null=True, default=timezone.now())
    title = models.CharField('job position', max_length=60)
    email = models.EmailField()
    salary = models.DecimalField(null=True, max_digits=18, decimal_places=2)

Core Field options:
    initial
    label
    help_text
    widdget
    localize
    
    required
    
    validators
    error_messages
    
    
Fields:
    ComboField - validate against a list of fields (a field is a validator in django term)
    MultipleValueField
    SplitDateTimeField
    
"""
from django import forms

from django.utils import timezone

class SillyContactForm(forms.Form):
    """
        validate a single field:
            form = SillyContactForm()
            form.fields['first_name'].clean('') -> 'required' error
            form.fields['first_name'].clean('a') -> u'a'
            
    """
    CONTACT_NAME_OPTS = {'min_length': 1, 'max_length': 20}
    
    #id = forms.IntegerField(required=False)
    
    first_name = forms.CharField(help_text='Your First Name', **CONTACT_NAME_OPTS)
    last_name = forms.CharField(**CONTACT_NAME_OPTS)
    
    title = forms.CharField(required=False)
    email = forms.EmailField(required=True, error_messages={'invalid': 'please enter a valid email address', 'required': 'email address cannot be blank'})
    salary = forms.DecimalField(required=False, max_digits=19, decimal_places=2)
    
    dob = forms.DateField(required=False, input_formats=['%m/%d/%y', '%Y-%m-%d'], initial=timezone.now(), error_messages={'invalid': 'invalid dob'})
    

from ajax_demo.models import SillyContact

class ContactForm(forms.ModelForm):
    class Meta:
        model = SillyContact
        fields = ['first_name', 'last_name', 'title', 'email', 'salary', 'dob'] #default is '__all__'
        
        #exlude = [...]
        #
        #
        # widgets, labels, help_texts, error_messages for further customization form display
        #
        #
        
        
    