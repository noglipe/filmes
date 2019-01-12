import requests
import json

class Requisicao():
 
    def __init__(self):
        self.key = 'apikey=1582e3cf'
        self.link = 'http://www.omdbapi.com/?'
        
    
    def Pesquisa_titulo(self, titulo):
        self.titulo = '&t='+ titulo
        self.link = self.link + self.key + self.titulo

        self.requisicao = requests.get(self.link)
        self.dicionario = json.loads(self.requisicao.text)

    def Exibir(self):
        print('Titulo: ', self.dicionario["Title"])
        print('Ano: ', self.dicionario["Year"])
        print('Genero: ', self.dicionario["Genre"])
