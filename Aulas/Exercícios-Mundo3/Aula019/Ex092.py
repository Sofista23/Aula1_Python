p={}
p["nome"]=input("Nome:")
p["ano"]=int(input("Data de Nascimento:"))
p["idade"]=2021-p["ano"]
p["ctps"]=int(input("Carteira de Trabalho (0 não tem):"))

if p["ctps"]!=0:
    p["contratação"]=int(input("Ano de Contratação:"))
    p["salario"]=int(input("Salário: R$"))
    tpcontrata=2021-p["contratação"]
    aposenta=45-tpcontrata
    print("-="*30)
    print(f"Você trabalho a {tpcontrata} ano(s) e faltam {aposenta} ano(s) para você se aposentar.")

else:
    print("-="*30)
    print("Você ainda não tem carteira de trabalho.")

print(p)

for k,v in p.items():
    print(f"{k} tem como valor {v}.")