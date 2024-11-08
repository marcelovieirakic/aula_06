# Solicita uma lista de números separados por vírgula
entrada = input("Digite uma lista de números separados por vírgula: ")

# Divide a entrada em uma lista de strings
numeros_texto = entrada.split(",")

# Cria uma lista para armazenar os números convertidos
numeros = []

# Tenta converter cada elemento para inteiro
for item in numeros_texto:
    try:
        # Remove espaços e converte para inteiro
        numero = int(item.strip())
        # Adiciona à lista de números
        numeros.append(numero)
    except ValueError:
        # Se a conversão falhar, exibe uma mensagem de erro e interrompe o script
        print(f"Erro: '{item}' não é um número inteiro válido.")
        break
else:
    # Se todos os elementos forem convertidos com sucesso, exibe a lista
    print("Lista de números inteiros:", numeros)
