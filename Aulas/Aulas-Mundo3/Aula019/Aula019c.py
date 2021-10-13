estado={}
brasil=[]
for c in range(0,3):
    estado["uf"]=input("Unidade Federativa:")
    estado["sigla"]=input("Sigla:")
    brasil.append(estado.copy())
for c in brasil:
    for k,v in c.items():
        print(f"O campo {k} tem valor {v}.")