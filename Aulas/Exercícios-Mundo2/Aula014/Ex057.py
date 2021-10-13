s=input("Digite seu sexo [m/f]: ").upper()
while s not in "MF":
    s=input("Dados inválidos, Digite novamente seu sexo [m/f]: ").upper()
if s=="M":
    print("Seu sexo é masculino.")
else:
    print("Seu sexo é feminino.")