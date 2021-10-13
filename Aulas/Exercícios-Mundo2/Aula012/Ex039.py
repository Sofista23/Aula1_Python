id=float(input("Digite sua idade:"))
if id<18:
    x=18-id
    print("Ainda não é seu momento de se alistar, mas falta(m) {0} ano(s) para se alistar.".format(x))
elif id==18:
    print("Já é o momento de você se alistar.")
else:
    x=id-18
    print("Já passou da hora de você se alistar, passou(m) {0} ano(s) para se alistar.".format(x))