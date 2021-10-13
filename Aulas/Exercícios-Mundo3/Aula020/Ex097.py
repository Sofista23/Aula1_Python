def escreva(txt):
    print("~"*len(txt))
    print(txt)
    print("~"*len(txt))

while True:
    print("-="*25)

    t=input("Escreva uma frase qualquer:")

    escreva(t)

    print("-="*25)
    
    esc=input("Continua[s/n]").strip().upper()[0]
    if esc=="N":
        break