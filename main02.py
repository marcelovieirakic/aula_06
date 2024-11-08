while True:
    try: 
        nome = input("digite o seu nome: ")
        idade = int(input("digite a sua idade: "))
        if not nome.isalpha():
            raise ValueError("voce nao digitou um nome valido")
        
        if isinstance(idade, int):
                print("voce digitou uma idade valida")
        else:
                print("voce digitou uma idade invalida")

        nome_maisculo = nome.upper()
        print(nome_maisculo)
        print(idade)
        break
    except ValueError as e:
        print(e)