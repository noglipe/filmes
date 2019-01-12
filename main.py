import sys

from requisicao import Requisicao

argumento = sys.argv

requisicao = Requisicao()

requisicao.Pesquisa_titulo(sys.argv[1])
requisicao.Exibir()