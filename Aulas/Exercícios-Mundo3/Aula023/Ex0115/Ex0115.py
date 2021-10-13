import menu
from time import sleep
import cadastros

while True:
    res=menu.menu(["Mostrar Cadastros","Cadastrar","Encerrar Programa"])
    
    if res==1:
        print("")
        menu.cabeçalho("Opção 1")
        print(cadastros.cadastro())
        print("")
    elif res==2:
        print("")
        menu.cabeçalho("2")
        print(cadastros.cadastrar())
        print("")
    elif res==3:
        print("")
        menu.cabeçalho("Sistema Encerrado!")
        break
    else:
        menu.cabeçalho("Erro! Dados Inválidos!")
    sleep(1)