def cadastrar():
    cad=input("Digite Nome:")
    return cad



def cadastro(*nomes):
    if len(nomes)>=1:
        c=1
        for item in nomes:
            print(f"{c} - {item}")
            c+=1
    else:
        return "Nenhuma pessoa cadastrada."