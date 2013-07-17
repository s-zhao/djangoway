"""
if rename this script to serializers.py, runscript will error out with following:
    SyntaxError: invalid syntax (serializers.py, line 23)

guess, this may be due to the fact runscript pre-importing all dependence modules 


http://django-rest-framework.org/api-guide/serializers.html
    Dynamically modifiying fields
    
"""

from polls.models import Poll, Choice

from django.utils import timezone
from rest_framework import serializers, renderers, parsers

import datetime, StringIO, pprint

class ChoiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Choice
        depth = 0
        
class PollSerializer(serializers.ModelSerializer):
    
    #
    #relation - tell serializer how to deserialize 'choice_set'
    #
    choice_set = serializers.RelatedField(many=True) #optionally, set read_only=True 
    #choice_set = serializers.PrimaryKeyRelatedField(many=True, read_only=True) #same as above
    
    #
    # extra fields for serialization .. if needed
    #
    # explicitly specify how a model field should be serialized...
    #
    class Meta:
        model = Poll
        depth = 1
        fields = ('id', 'question', 'pub_date', 'choices')
        #
        # other options:
        #   use related_name in Choice model
        #       poll = models.ForeignKey(Poll, related_name='choices')
        #
        #
    def choices(self):
        pass
        
class DynamicFieldsModelSerializer(serializers.ModelSerializer):
    """
    A ModelSerializer that takes an additional `fields` argument that
    controls which fields should be displayed.
    """

    def __init__(self, *args, **kwargs):
        # Don't pass the 'fields' arg up to the superclass
        fields = kwargs.pop('fields', None)

        # Instatiate the superclass normally
        super(DynamicFieldsModelSerializer, self).__init__(*args, **kwargs)

        if fields:
            # Drop any fields that are not specified in the `fields` argument.
            allowed = set(fields)
            existing = set(self.fields.keys())
            for field_name in existing - allowed:
                self.fields.pop(field_name)
             
class ChoiceSerializer(DynamicFieldsModelSerializer):
    class Meta:
        model = Choice
        fields = ('choice_text',)
        
def run1():
    queryset = Poll.objects.all()
    print queryset
    print
    
    serializer = PollSerializer(queryset, many=True)
    for entry in serializer.data:
        entry = dict(entry)
        print(entry)
        print
    print
    
    json = renderers.JSONRenderer().render(serializer.data)
    print 'json: ', json
    print
    
    data = parsers.JSONParser().parse( StringIO.StringIO(json) )
    serializer = PollSerializer(data=data, many=True)
    
    assert(serializer.is_valid())
    polls = serializer.object
    print polls
    print
    for p in polls:
        print type(p)
        print p.choice_set.all()

run = run1