toatl=0
gols=[]
jog={}

jog["nome"]=input("Nome do Jogador:")
jog["qtnPartidas"]=int(input(f"Quantidade de partidas que {jog['nome']} jogou:"))

for c in range(0,jog["qtnPartidas"]):
    qtnGols=int(input(f"Quantos gols foram feitos na parida {c+1}:"))
    toatl+=qtnGols
    gols.append(qtnGols)

jog["gols/partida"]=gols

jog["total"]=toatl

print("-="*45)

print(jog)

print("-="*45)

for k,v in jog.items():
    print(f"O campo {k} tem o valor {v}")

print("-="*45)

print(f"O jogador {jog['nome']} jogou {jog['qtnPartidas']} partida(s).")

for q,r in enumerate(jog["gols/partida"]):
    print(f"Na partida {q+1}, fez {r} gol(s).")

print(f"Fez um total de {jog['total']} gol(s).")