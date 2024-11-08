try: 
    numero_1 = int(input("digite o numero para divisao numerador: "))
    numero_2 = int(input("digite outro numero para divisao denominador: "))
    operacao = numero_1/numero_2
    print(operacao)
except ValueError as e:
    print(e)
    # print("algo foi digitado errado")
