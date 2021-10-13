def leiaInt(x=0):
    ok=False
    val=0
    while True:
        num=input(x)
        if num.isnumeric():
            val=int(num)
            ok=True
        else:
            print("Erro, digite um número inteiro válido.")
        if ok==True:
            break
    return val

n=leiaInt("Digite um número:")
print(f"Você digitou o valor {n}.")
