t1=("Taiga","Ryuji","Minori","Ami","Kitamura","Makoto","Mitsuha","Taki","Eren","Mikasa","Armin")
for c in t1:
    print(f"\nNa palavra {c} temos ",end="")
    for l in c:
        if l.lower() in "aeiou":
            print(l,end=" ")
print("Fim do Programa.")