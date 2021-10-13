num=int(input("Digite um número:"))
esc=int(input("Escolha entre 1, 2 e 3 para a conversão:"))
if esc==1:
    print("Você escolheru binário:")
    print(bin(num))
elif esc==2:
    print("Você escolheru octal:")
    print(oct(num))
elif esc==3:
    print("Você escolheu hexadecimal:")
    print(hex(num))