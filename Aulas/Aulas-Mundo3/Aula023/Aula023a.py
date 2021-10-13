try:
    a=int(input('Numerador:'))
    b=int(input('Denominador:'))

    r=a/b

except (ValueError,TypeError):
    print("Dados inválidos!!!")
except ZeroDivisionError:   
    print("Não é possível dividir por zero!!!")
except KeyboardInterrupt:
    print("Dados não informados!!!")
except Exception as erro:
    print(f"O erro encontrado foi {erro.__cause__}")

else:
    print(f"O resultado é {r:.1f}.")

finally:
    print("Obrigado por usar nosso programa!")