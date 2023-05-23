from django.http import response
from django.test import SimpleTestCase #estou usando simple pq n estamos usando database

# Create your tests here.
class SimpleTests(SimpleTestCase):
    def test_home_pages_code(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200) #200 é o padrao qnd request HTTP é um sucesso

    def test_about_status_code(self):
        response = self.client.get('/about/')
        self.assertEqual(response.status_code, 200)

