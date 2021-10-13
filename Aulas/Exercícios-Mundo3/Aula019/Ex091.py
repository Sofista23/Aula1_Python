from random import randint
from time import sleep
from operator import itemgetter
jogadores={"jog1":randint(1,6),"jog2":randint(1,6),"jog3":randint(1,6),"jog4":randint(1,6)}
ranking={}
for k,v in jogadores.items():
    print(f"O {k} tirou {v} no dado.")
ranking=sorted(jogadores.items(),key=itemgetter(1),reverse=True)
print("-="*30)
for i,v in enumerate(ranking):
    print(f"{i+1} lugar: {v[0]} com {v[1]}")
print(ranking)