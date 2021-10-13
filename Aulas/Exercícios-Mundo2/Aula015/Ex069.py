s=""
i=0
maior=0
qhomens=0
qmulheresmenores=0
esc=""
while True:
    s=input("Digite seu sexo [m/f]: ").upper().strip()
    i=int(input("Digite sua idade: "))
    if i>=18:
        maior += 1
    if s=="M":
        qhomens += 1
    if s=="F":
        if i<=20:
            qmulheresmenores += 1
    esc=input("Continuar Cadastros [s/n]? ").upper().strip()
    if esc=="N":
        break
print(f"Tem {maior} pessoa(s) maiores de idade.")
print(f"{qhomens} homem(s) foi cadastrado(s).")
print(f"Tem {qmulheresmenores} mulher(d) menor(s) de 20 anos.")
print("Fim do Cadastro!")