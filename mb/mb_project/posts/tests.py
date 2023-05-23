from django.test import TestCase
from matplotlib.pyplot import text
from .models import Post
from django.urls import reverse
# Create your tests here.

class PostModelTest (TestCase):

    def setUp (self):
        #criando uma nova database que contem a entrada text
        Post.objects.create(text='just a test')

    #primeiro teste
    #checa se a databse realmente contem a str
    def test_text_content (self):
        post = Post.objects.get(id=1)
        #variável para guardar a string contida em post.text
        expected_object_name = f'{post.text}'
        #assert equal verifica se há igualdade com os dois parametroa
        self.assertEqual(expected_object_name,'just a test')

#criando uma classe para testar a homepage 
class HomePageViewTest(TestCase):

    def setUp(self):
        Post.objects.create(text='this is another test')

    #testando se existe a url mesmo e verificando a resposta http
    def test_view_url_exists_at_proper_location(self):
        resp = self.client.get('/')
        self.assertEqual(resp.status_code, 200)

    #testando se está usadno homepageview como the view
    def test_view_url_by_name(self):
        resp = self.client.get(reverse('home'))
        self.assertEqual(resp.status_code, 200)

    #testanto se esta realmente usando home.html como template
    def test_view_uses_correct_template(self):
        resp = self.client.get(reverse('home'))
        self.assertEqual(resp.status_code, 200)
        self.assertTemplateUsed(resp,'home.html')

