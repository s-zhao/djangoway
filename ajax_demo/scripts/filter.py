
from ajax_demo.models import SalariedContact, SillyContact

def run():
    
    request = {'salary': '10', 'last_name': 'smith'}
    
    f = SalariedContact(request, queryset=SillyContact.objects.all())
    
    print f
    print f.form
    print
    for o in f:
        print o, o.id, o.salary