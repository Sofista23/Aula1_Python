val=[7,5,4,8]
def dobra(lst):
    pos=0
    while pos<len(lst):
        lst[pos]*=2
        pos+=1
dobra(val)
print(val)


def soma(*valores):
    s=0
    for c in valores:
        s+=c
    print(f"A soma dos valore {valores} é {s}.")
soma(5,4,8)