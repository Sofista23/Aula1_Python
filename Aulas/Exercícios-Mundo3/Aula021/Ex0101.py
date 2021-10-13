def vota(ano):
    idade=2021-ano
    if idade<16:
        return "Voto negado."
    elif idade<18:
        return "Voto Opicional."
    elif idade>65:
        return "Voto Opicional." 
    else:
        return "Voto Obrigatório."

nas=int(input("Digite sua data de nascimento:"))
idade=2021-nas
print("-="*20)

print(f"Com {idade} anos: {vota(nas)}")