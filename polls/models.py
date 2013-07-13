from django.db import models
from django.utils import timezone
import datetime

# Create your models here.

class Poll(models.Model):
    question = models.CharField(max_length=200)
    pub_date = models.DateTimeField('published date')
    
    def __unicode__(self):
        return self.question
        
    def was_published_recently(self):
        return self.pub_date > timezone.now() - datetime.timedelta(hours=2)
    was_published_recently.admin_order_field = 'pub_date'
    was_published_recently.boolean = True
    was_published_recently.short_description = 'recently published?'
        

class Choice(models.Model):
    poll = models.ForeignKey(Poll)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)
    
    def __unicode__(self):
        return u'%s > %s' % (self.poll.question, self.choice_text)
        
        