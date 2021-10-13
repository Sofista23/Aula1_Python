def resumo(x,a,d,ajuste="R$"):

    print("-"*35)
    
    print("          RESUMO DO VALOR")

    print("-"*35)

    dobro=x*2

    metade=x/2

    porCem01=x*a/100
    aumento=x+porCem01

    porCem02=x*d/100
    diminui=x-porCem02

    print(f"Preço Analizado: {ajuste}{x}")
    print(f"O dobro do preço: {ajuste}{dobro}")
    print(f"A metade do preço: {ajuste}{metade}")
    print(f"{a}% de aumento: {ajuste}{aumento}")
    print(f"{d}% de redução: {ajuste}{diminui}")

    print("-"*35)