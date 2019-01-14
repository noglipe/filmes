import sys

from requisicao import Requisicao

argumento = sys.argv
requisicao = Requisicao()
titulo =''

if len(sys.argv) > 1:
    for arg in argumento:
        if not arg == 'main.py':
            titulo += arg + "+"

    #removendo o '+' excedente na construção da string
    titulo = titulo[:-1]

    if requisicao.Pesquisa_titulo(titulo):
        requisicao.Exibir()
    else:
        print("Nenhum título encontrado")

else:
    print('Favor digitar o Título a ser pesquisado. não é necessário \'\' \nExemplo: python main.py nome do filme')
    exit()



