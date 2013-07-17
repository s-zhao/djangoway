from django.db import models
from django.forms import widgets

from rest_framework import serializers

from pygments.lexers import get_all_lexers
from pygments.styles import get_all_styles

LEXERS = [item for item in get_all_lexers() if item[1]]
LANGUAGE_CHOICES = sorted([(item[1][0], item[0]) for item in LEXERS])
STYLE_CHOICES = sorted([(item, item) for item in get_all_styles()])

class SnippetSerializer(serializers.Serializer):
    pk = serializers.Field() 
    title = serializers.CharField(requred=False, max_length=100)
    code = serializers.CharField(max_length=100000, widget=widgets.TextArea)
    linenos = serializers.BooleanField(required=False)
    language = serializers.ChoiceField(choices=LANGUAGE_CHOICES, default='python')
    style = serializers.ChoiceField(choices=STYLE_CHOICES, default='friendly')
    
    def xrestore_object(self, attrs, instance=None):
        if instance:
            instance.title = attrs.get('', instance.)
            instance.title = attrs.get('', instance.)
            instance.title = attrs.get('', instance.)
            instance.title = attrs.get('', instance.)
            instance.title = attrs.get('', instance.)
            instance.title = attrs.get('', instance.)
            instance.title = attrs.get('', instance.)
            return instance
        #return Snippet(**attrs)
        