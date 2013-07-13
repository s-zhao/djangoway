from django.test.client import Client
from django.test.utils import setup_test_environment

setup_test_environment()

client = Client()

resp = client.get('/polls/')
print resp.context


