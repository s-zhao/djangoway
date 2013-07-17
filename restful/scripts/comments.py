
from rest_framework import serializers, renderers, parsers

import datetime, StringIO

class Comment(object):
    def __init__(self, email, content, created=None):
        self.email = email
        self.content = content
        self.created = created or datetime.datetime.now()

class CommentSerializer(serializers.Serializer):
    email = serializers.EmailField()
    content = serializers.CharField(max_length=200)
    created = serializers.DateTimeField()
    
    def restore_object(self, attrs, instance=None):
        if instance:
            instance.email = attrs.get('email', instance.email)
            instance.content = attrs.get('content', instance.content)
            instance.created = attrs.get('created', instance.created)
            return instance
        return Comment(**attrs)
    
    # just like django .clean_{fieldname}, you can do following to validate a field.    
    #def validate_{attrname}(self, attrs, source):
    #

def run():        
    comment = Comment(email='leila@example.com', content='foo bar')

    serializer = CommentSerializer(comment)
    print 'the data for serialization: ', serializer.data
    print
    
    json = renderers.JSONRenderer().render(serializer.data)
    print json
    print
    
    stream = StringIO.StringIO(json)
    data = parsers.JSONParser().parse(stream)
    print 'data: ', data
    print
    
    serializer = CommentSerializer(data=data)
    print 'is valid: ', serializer.is_valid()
    print
    print 'deserialized: ', serializer.object
    print
    
    #
    # deserialize and update object
    #
    comment = Comment('joe@j.com', 'hello')
    serializer = CommentSerializer(comment, data=data)
    serializer.is_valid()
    print serializer.object
    print serializer.data
    print
    
    #
    #partial data - always call .is_valid() otherwise, instance will not be updated.
    #
    serializer = CommentSerializer(comment, data={'email': 'x@y.com'}, partial=True)
    print serializer.is_valid()
    print serializer.errors
    print serializer.data
    print
    
    #
    #
    #
    serializer = CommentSerializer(data={'email': 'x@y.com'})
    print 'is valid: ', serializer.is_valid()
    print serializer.errors
    print
    
    print 
    print 'serializing multipe objects...'
    print
    comments = [ Comment('joe-%s@j.com' % i, 'hello-%s' % i) for i in range(1,4)] 
    serializer = CommentSerializer(comments, many=True)
    print 'data: ', serializer.data
    print
    
    json = renderers.JSONRenderer().render(serializer.data)
    print 'json: ', json
    print
    
    stream = StringIO.StringIO(json)
    data = parsers.JSONParser().parse(stream)
    serializer = CommentSerializer(data=data, many=True)
    if serializer.is_valid():
        print 'deserialized: ', serializer.object
    else:
        serializer.errors
    

    
    