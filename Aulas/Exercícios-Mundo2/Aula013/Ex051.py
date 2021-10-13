#PA
pt=int(input("Pimeiro Termo:"))
r=int(input("Razão:"))
d=pt+(11-1)*r
for c in range(pt,d,r):
    print("{0}".format(c),end=",")