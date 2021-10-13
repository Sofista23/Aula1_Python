def calc(a,b):
    s=a+b
    print(f"A soma entre {a} e {b} é {s}.")
while True:
    x=int(input("Digite um número:"))
    y=int(input("Digite mais um número:"))
    calc(x,y)
    esc=input("Continua[s/n]:").strip().upper()[0]
    if esc=="N":
        break