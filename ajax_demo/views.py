# Create your views here.
from django.http import HttpResponse, HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.shortcuts import render, redirect, get_object_or_404


from ajax_demo.models import SillyContact
from ajax_demo.forms import SillyContactForm

def index(request):
    
    return render(request, 'ajax_demo/index.html')
    
def contacts(request):
    contacts = SillyContact.objects.all()
    context = {'contacts': contacts}
    
    return render(request, 'ajax_demo/fragments/contacts.html', context)
    
def contact_new(request):
    """
    show form for entering new record
    """
    initials = {'first_name': 'John', 'last_name': 'Smith', 'email': 'jsmith@j.com'}
    context = {'contact_form': SillyContactForm(initial=initials, prefix='silly')}
    
    return render(request, 'ajax_demo/fragments/contact_form.html', context)
    
def contact_save_new(request):
    """
    save new - can be combined into 'save edit'
    """
    #print 'method: ', request.method #GET, POST ... in upper case
    #print 'is_secure: ', request.is_secure()
    #print 'is_ajax: ', request.is_ajax()
    
    if request.method != 'POST':
        return HttpResponseRedirect( reverse('ajax-demo:contact-new') )
        
    form = SillyContactForm(request.POST, prefix='silly') #data, is_valid(), is_bound, is_multipart, cleaned_data, changed_data, prefix ...
    #print 'is-bound: ', form.is_bound
    
    if not form.is_valid():
        context = {'contact_form': form}
        return render(request, 'ajax_demo/fragments/contact_form.html', context)
        
    #for f in form.fields:
    #    print f
    
    #cleaned_data dict is just good for create record
    silly, created = SillyContact.objects.get_or_create(**form.cleaned_data)

    return HttpResponseRedirect( reverse('ajax-demo:contact-details', kwargs={'pk': silly.id}) )

    
def contact_details(request, pk):
    """
    show detail 
    """
    silly = SillyContact.objects.get(pk=pk)
    
    data = {}
    fields = silly._meta.get_all_field_names()
    for field in fields:
        data[field] = getattr(silly, field)
        
    context = {'contact_form': SillyContactForm(initial=data, prefix='silly'),
               'contact_record': silly}
    
    return render(request, 'ajax_demo/fragments/contact_detail.html', context)
    
def contact_edit(request, pk):
    """
    show form for edit
    """
    silly = SillyContact.objects.get(pk=pk)
    
    data = {}
    fields = silly._meta.get_all_field_names()
    for field in fields:
        data[field] = getattr(silly, field)
        
    context = {'contact_form': SillyContactForm(initial=data, prefix='silly'), 'contact_record': silly}
    
    return render(request, 'ajax_demo/fragments/contact_edit.html', context)
    
def contact_save_edit(request):
    """
    save edit - it is not DRY but we do need to distinguish UPDATE from CREATE for handling UPDATE logic
    """
    if request.method != 'POST':
        return HttpResponseForbidden()
        
    pk = request.POST.get('id', None)
    if not pk:
        return HttpResponseForbidden()
    
    silly = get_object_or_404(SillyContact, pk=pk)
    
    form = SillyContactForm(request.POST, prefix='silly') 
    if not form.is_valid():
        context = {'contact_form': form, 'contact_record': silly}
        return render(request, 'ajax_demo/fragments/contact_edit.html', context)

    #
    #save - would be nice if django provides silly.save(**form.cleaned_data)
    #
    [setattr(silly, k, v) for k, v in form.cleaned_data.items()]
    silly.save()
    
    return redirect('ajax-demo:contact-details', pk=pk)

    
        