val=[]

def maior(v):
    ma=max(v)
    print(f"O maior valor entre {v} é {ma}.")

while True:
    x=int(input("Digite um número:"))
    val.append(x)
    esc=input("Continua[s/n]:").upper().strip()[0]
    if esc=="N":
        break

maior(val)