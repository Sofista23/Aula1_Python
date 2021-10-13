r1=int(input("Digite a 1° reta do triângulo:"))
r2=int(input("Digite a 2° reta do triângulo:"))
r3=int(input("Digite a 3° reta do triângulo:"))
if r1==r2 and r2==r3:
    print("Esse é um triângulo EQILÁTERO.")
elif r1==r2 and r1!=r3:
    print("Esse triângulo é ISÓCELES.")
elif r1==r3 and r1!=r2:
    print("Esse triângulo é ISÓCELES.")
elif r2==r3 and r2!=r1:
    print("Esse triângulo é ISÓCELES.")
else:
    print("Esse triângulo é ESCALENO.")