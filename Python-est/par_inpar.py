def verificar_pares_impares():
    while True:
        entrada = input("Digite um número inteiro ou 'sair' para encerrar: ")

        # Verificar se o usuário quer sair
        if entrada.lower() == 'sair':
            print("Encerrando o programa.")
            break

        try:
            # Tentar converter a entrada para inteiro
            numero = int(entrada)
            
            # Verificar se o número é par ou ímpar
            if numero % 2 == 0:
                print(f"{numero} é par.")
            else:
                print(f"{numero} é ímpar.")
        
        except ValueError:
            # Tratamento de erro para entradas não numéricas
            print("Erro: Por favor, insira um número inteiro válido.")

# Chamada da função para executar o programa
verificar_pares_impares()
