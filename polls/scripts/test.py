from django.test.client import Client
from django.test.utils import setup_test_environment

setup_test_environment()

client = Client()



def run():
    resp = client.get('/polls/')

    print resp.context
    print
    print resp.content
    print

