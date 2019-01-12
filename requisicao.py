import requests
import json

class Requisicao():
 
    def __init__(self):
        arquivo = open("meu.txt", 'r')
        self.key = arquivo.read()
        self.link = 'http://www.omdbapi.com/?'
        
    
    def Pesquisa_titulo(self, titulo):
        self.titulo = '&t='+ titulo
        self.link = self.link + self.key + self.titulo

        self.requisicao = requests.get(self.link)
        self.dicionario = json.loads(self.requisicao.text)
        
        if self.dicionario['Response'] == 'False':
            return False
        else:
            return True

    def Exibir(self):
        #Testar se o link está sendo montado corretamente
        #print(self.link)
        self.tipo = str(self.dicionario["Type"])

        print("Titulo: ", self.dicionario["Title"], " - ", self.tipo.upper() )
        print('Ano: ', self.dicionario["Year"])
        print('Genero: ', self.dicionario["Genre"])
        if self.tipo == 'movie':
            print('Duração: ', self.dicionario["Runtime"])