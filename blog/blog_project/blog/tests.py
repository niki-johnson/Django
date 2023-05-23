import email
from django.test import TestCase
from django.urls import reverse
from django.contrib.auth import get_user_model #referencia o user ativo
from .models import Post

# Create your tests here.

class BlogTests (TestCase):

    def setUp (self):

        self.user = get_user_model().objects.create_user(username = 'testuser', email = 'test@email.com', password = 'secret')

        #criando amostra de um post no blog
        self.post = Post.objects.create(title = 'A good title', body = 'Nice body content', author = self.user,)

    def test_string_representation(self):
        '''testa se realmente o conteúdo é string'''
        post = Post(title='A sample title')

        self.assertEqual(str(post), post.title)

    def test_post_content(self):
        '''testa os conteúdos, se estão corretos, testa o titulo, conteúdo e autor'''
        self.assertEqual(f'{self.post.title}', 'A good title')

        self.assertEqual(f'{self.post.author}', 'testuser')

        self.assertEqual(f'{self.post.author}', 'Nice body content')

    def test_post_detail_view(self):
        '''testa se nossa pagina de post esta funcionando bem'''
        response = self.client.get('/post/1/')
        no_response = self.client.get('/post/10000/')

        self.assertEqual(response.status_code, 200)

        self.assertEqual(no_response.status_code, 404)

        self.assertContains(response, 'A good title')

        self.assertTemplateUsed(response, 'post_detail.html')

    def test_post_list_view(self):
        '''testa se a homepage existe, se contem o conteudo e se usa o template certo'''
        response = self.client.get(reverse('home'))
        
        self.assertEqual(response.status_code, 200)

        self.assertContains(response, 'Nice body content')

        self.assertTemplateUsed(response, 'home.html')