aluno={}
aluno["Nome"]=input("Nome:")
aluno["Nota 1"]=float(input("Nota 1:"))
aluno["Nota 2"]=float(input("Nota 2:"))
aluno["Média"]=(aluno["Nota 1"]+aluno["Nota 2"])/2
for k,v in aluno.items():
    print(f"{k} é igual a {v}.")
if aluno["Média"]>=7:
    print("Aprovado!")
else:
    print("Reprovado!")