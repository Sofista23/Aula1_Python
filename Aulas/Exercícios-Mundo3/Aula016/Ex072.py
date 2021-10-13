t=("zero","um","dois","três","quatro","cinco","seis","sete","oito","nove","dez","onze","doze","treze","quatorze","quinze","dezesseis","dezessete","dezoito","dezenove20","vinte")
while True:
    esc=int(input("Digite um número de 0 a 20:"))
    if  0<=esc<=20:
        print(f"Você digitou o valor {t[esc]}.")
    esc2=input("Você quer continuar [s/n]:").strip().upper()
    if esc2=="N":
        break
print("Obrigado por perder seu tempo conosco.")