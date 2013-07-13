"""
This file demonstrates writing tests using the unittest module. These will pass
when you run "manage.py test".

Replace this with more appropriate tests for your application.
"""
from django.utils import timezone
from polls.views import Poll

#from django.test.utils import setup_test_environment
from django.test.client import Client
from django.test import TestCase

setup_test_environment()
client = Client()

class SimpleTest(TestCase):
    def test_basic_addition(self):
        """
        Tests that 1 + 1 always equals 2.
        """
        self.assertEqual(1 + 1, 2)
        
    def test_save(self):
        print 'all polls: ', Poll.objects.all()
        poll = Poll.objects.create(question='Is Pittsburgh too old - %s ?' % timezone.now(), pub_date=timezone.now())
        #poll.save()
        print 'poll: ', poll.id
        print "total: ", Poll.objects.all()
        self.assertEqual(1 + 1, 2)

    def test_get_or_create(self):
        poll = Poll(question='Is Pittsburgh too old??', pub_date=timezone.now())
        poll.save()
        p, created = Poll.objects.get_or_create(question='Is Pittsburgh too old??', pub_date=timezone.now())
        print p, created
        #self.assertFalse(created)
        