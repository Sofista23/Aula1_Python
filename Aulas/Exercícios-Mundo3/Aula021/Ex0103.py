def ficha(nome="",pontos=""):
    if nome=="" and pontos=="":
        print(f"O jogador <desconhecido> fez 0 ponto(s).")
    elif nome=="":
        print(f"O jogador <desconhecido> fez {pontos} ponto(s).") 
    elif pontos=="":
        print(f"O jogador {nome} fez 0 ponto(s).")
    else:
        print(f"O jogador {nome} fez {pontos} ponto(s).")

n=input("Digite seu nome:")
p=input("Quntidade de pontos feitos:")

ficha(n,p)