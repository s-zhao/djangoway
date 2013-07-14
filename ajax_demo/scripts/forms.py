from ajax_demo.forms import SillyContactForm
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
    
    
    