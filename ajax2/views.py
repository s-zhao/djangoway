# Create your views here.

#http://django-tastypie.readthedocs.org/en/latest/authorization.html#usage

from django.http import HttpResponse, HttpResponseForbidden, HttpResponseRedirect
from django.shortcuts import render_to_response, render
from django.core.urlresolvers import reverse
from rest_framework import parsers, renderers, serializers
from rest_framework.response import Response

from ajax2.models import SillyBlog

#
# django + angular
#
def ng_way(request):
    records = api_list_records(request)
    serializer = SillyBlogSerializer(records, many=True)
    
    json = renderers.JSONRenderer().render(serializer.data)
    
    context = {'records': json}
    
    context = {}
    return render(request, 'ajax2/ng.html', context)

    
#
# django + jQuery + ajax
#

#
# HTTP request
#
def list_record(request):
    records = api_list_records(request)    
    context = {'records': records}
    return render(request, 'ajax2/records.html', context)

def blogs(request):
    records = api_list_records(request)
    data=SillyBlogSerializer(records).data
    return _response(request, data)
    
def get_record(request, pk): 
    blog = api_new_record if pk == '0' else api_get_record(pk)        
    context = {'blog': blog}
    return render(request, 'ajax2/editor.html', context) 
        
def save_record(request, *args, **kwargs):
    if request.method != 'POST':
        raise HttpResponseForbidden()
        
    pk = kwargs.get('pk', '')        
    blog = api_get_record(pk)
    
    #
    # RULE - allow vs exclude - data access rules on FIELD level
    #
    allow = ['subject', 'body']
    exclude = ['creator_account', 'owner_account']
    data = {}
    for field in allow:
        if field in request.POST:
            data[field] = request.POST[field]
    
    resp_data = api_save_record(blog, data) or SillyBlogSerializer(blog).data
    return _response(request, resp_data)

#
# let rest_framework handle HTTP negotiation and data exchange
#        
from rest_framework.decorators import api_view

@api_view(['GET', 'POST']) 
def _response(request, data):
    return Response(data)

#
# serializers
#    
class SillyBlogSerializer(serializers.ModelSerializer):
    class Meta:
        model = SillyBlog
        
#
# access rules - filters
#
#
def api_list_records(request):
    """ filters
    . range
    . authorization
    . searchParams like, subject__icontains = 'test'
    """
    queryset = SillyBlog.objects.all()
    return queryset
    
#
# require - read acces
# require - write access
# require - owner ship
# require - delete access
# 
def api_get_record(pk):    
    try:
        return SillyBlog.objects.get(pk=pk)
    except SillyBlog.DoesNotExist:
        return api_new_record()
    
def api_new_record():
    return SillyBlog()
    
def api_save_record(record, data):
    return api_save_new(record, data) if record.id else api_update_record(record, data)
    
def api_save_new(record, data):
    form = _validate_record(record, data)
    if form.is_valid():
        form.save()
        return ""
    return {'errors': form.errors}
        
def api_update_record(record, data):
    form = _validate_record(record, data)
    if form.is_valid():
        form.save()
        return ""
    return {'errors': form.errors}

def _validate_record(record, data):
    form = SillyBlogForm(data, instance=record)
    #
    # record validator
    #
    return form
    
#
# validator
#    
from django import forms

class SillyBlogForm(forms.ModelForm):
    class Meta:
        model = SillyBlog
        #fields = (...)
        