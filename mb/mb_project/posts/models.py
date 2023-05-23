#help us build new database models, which will
#“model” the characteristics of the data in our database
from django.db import models

# Create your models here.

#creating a model to store the textual content of a message board post
class Post (models.Model):
    text = models.TextField() #.TextField especifica o tipo de conteudo que guarda

    def __str__(self):
        '''Mostra ao usuario os primeiros 50 caracters
        do campo de texto'''
        return self.text[:50]
