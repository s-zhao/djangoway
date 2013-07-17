from django.db import models

# Create your models here.

class SillyBlog(models.Model):
    subject = models.CharField(max_length=60)
    body = models.TextField(null=False, blank=False)
    
    def __unicode(self):
        return self.subject
        