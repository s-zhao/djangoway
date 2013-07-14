
from ajax_demo.models import SillyContact
from ajax_demo.forms import SillyContactForm, ContactForm
from django.core.validators import ValidationError

def min10(value):
    if len(value) < 10:
        raise 'Error, min 10'
        
def run():
    form = SillyContactForm()
    dob = form.fields['dob'].clean('01/12/13')
    print dob
    
    try:
        dob = form.fields['dob']        
        dob.clean('14/01/15')
    except ValidationError as e:    
        print e
    
    
    print 'test ModelForm'
    
    request = {
        'first_name': 'Bill',
        'last_name': 'SMith',
        'title': 'doer',
        'email': 'j@x.com',
        'dob': '1999-12-01', 
        'salary': 10000,
    }
    
    #
    # empty form with initial
    #
    form = ContactForm(request)
    print form
    print
    
    #
    # create a contact from request
    #
    contact = SillyContact()
    form = ContactForm(request, instance=contact)
    form.save()
    print contact, contact.id
    print
    
    #
    # create a contact from request, do not save
    #
    contact = SillyContact()
    form = ContactForm(request, instance=contact)
    form.save(commit=False)
    print contact, contact.id
    
    form.first_name = "bill2"
    print 'is valid: ', form.is_valid()
    form.save()
    #
    #form.save_m2m() #need this to commit m2m relation due to previous commit=False
    #
    print contact, contact.first_name, contact.id
    print
    
    #
    # get record for edit /<pk>/
    #
    form = ContactForm(instance=SillyContact.objects.get(pk=1))
    print form
    print form.id
    
