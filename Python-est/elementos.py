def solicitar_quantidade():
    """Solicita a quantidade de elementos para a lista e retorna o valor."""
    while True:
        try:
            quantidade = int(input("Insira a quantidade de elementos que deseja ter na lista: "))
            if quantidade < 0:
                print("Por favor, insira um número positivo.")
            else:
                return quantidade
        except ValueError:
            print("Entrada inválida. Por favor, insira um número inteiro.")

def ler_elementos(quantidade):
    """Lê os elementos da lista a partir da entrada do usuário."""
    elementos = []
    for i in range(quantidade):
        elemento = input(f"Digite o elemento {i + 1}: ")
        elementos.append(elemento)
    return elementos

def imprimir_lista(elementos):
    """Imprime a lista lida."""
    print("Lista lida:", elementos)

def buscar_numero(elementos):
    """Solicita um número para ser buscado na lista e conta quantas vezes aparece."""
    numero = input("Digite um número para ser buscado na lista: ")
    contagem = elementos.count(numero)
    print(f"O número {numero} aparece {contagem} vez(es) na lista.")

def main():
    """Função principal do programa."""
    while True:
        quantidade = solicitar_quantidade()
        elementos = ler_elementos(quantidade)
        imprimir_lista(elementos)
        buscar_numero(elementos)

        continuar = input("Deseja continuar? (s/n): ").lower()
        if continuar != 's':
            print("Programa encerrado.")
            break

if __name__ == "__main__":
    main()
