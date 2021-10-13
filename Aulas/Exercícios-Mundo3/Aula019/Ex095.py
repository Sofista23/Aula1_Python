toatl=0
gols=[]
jog={}
time=[]
while True:
    jog.clear()
    gols.clear()

    jog["nome"]=input("Nome do Jogador:")
    jog["qtnPartidas"]=int(input(f"Quantidade de partidas que {jog['nome']} jogou:"))

    for c in range(0,jog["qtnPartidas"]):
        qtnGols=int(input(f"Quantos gols foram feitos na parida {c+1}:"))
        toatl+=qtnGols
        gols.append(qtnGols)

    jog["gols/partida"]=gols

    jog["total"]=toatl

    time.append(jog.copy())

    esc=input("Continua[s/n]").strip().upper()[0]
    if esc=="N":
        break

print("-="*45)

for k,v in enumerate(time):
    print(f"{k}")
    for d in v.values():
        print(f"{str(d)}")
    print()

print("-="*45)