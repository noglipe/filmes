import sys

from requisicao import Requisicao

argumento = sys.argv
requisicao = Requisicao()
titulo =''

for arg in argumento:
    if not arg == 'main.py':
        titulo += arg + "+"

if requisicao.Pesquisa_titulo(titulo):
    requisicao.Exibir()
else:
    print("Nenhum título encontrado")

