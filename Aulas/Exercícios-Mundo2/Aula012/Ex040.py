n1=int(input("Digite sua 1° nota:"))
n2=int(input("Digite sua 2° nota:"))
n3=int(input("Digite sua 3° nota:"))
n4=int(input("Digite sua 4° nota:"))
med=(n1+n2+n3+n4)/4
if med<5:
    print("Aluno REPROVADO com média {0}.".format(med))
elif med>5 and med>7:
    print("Aluno vai para RECUPERAÇÃO com média {0}.".format(med))
else:
    print("Aluno APROVADO com média {0}.".format(med))