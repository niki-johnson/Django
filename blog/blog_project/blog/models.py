from django.db import models
#importando classe models
# Create your models here.

#criando a sublcasse post

class Post(models.Model):
    
    #limitando há uma máximo de 200 caracteres
    title = models.CharField(max_length = 200)

    #usando uma froeignkey oq significa que o usuario pode ser autor de diferentes blogs posts
    author = models.ForeignKey(
        'auth.User', 
        on_delete=models.CASCADE,

    )

    #tipo de data que estamos recebendo é do tipo texto e pode tero o tamanaho que quiser
    body = models.TextField()

    def __str__(self):
        
        return self.title

