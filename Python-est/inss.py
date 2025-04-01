def calcular_desconto_ir(salario_bruto, desconto_inss):
    # Calcular o salário base
    salario_base = salario_bruto - desconto_inss

    # Calcular o desconto de IR com base nas faixas
    if salario_base <= 1903.98:
        desconto_ir = 0.0
    elif salario_base <= 2826.65:
        desconto_ir = salario_base * 0.075 - 142.80
    elif salario_base <= 3751.05:
        desconto_ir = salario_base * 0.15 - 354.80
    elif salario_base <= 4664.68:
        desconto_ir = salario_base * 0.225 - 636.13
    else:
        desconto_ir = salario_base * 0.275 - 869.36

    return desconto_ir

def main():
    try:
        # Solicitar ao usuário o salário bruto e o desconto do INSS
        salario_bruto = float(input("Digite o valor do salário bruto: R$ "))
        desconto_inss = float(input("Digite o valor do desconto do INSS: R$ "))

        # Validar se os valores são positivos
        if salario_bruto < 0 or desconto_inss < 0:
            print("Erro: Insira valores positivos para o salário bruto e o desconto do INSS.")
            return

        # Calcular o desconto do IR
        desconto_ir = calcular_desconto_ir(salario_bruto, desconto_inss)

        # Exibir o resultado do desconto do IR
        print(f"O desconto do Imposto de Renda é: R$ {desconto_ir:.2f}")

    except ValueError:
        print("Erro: Por favor, insira valores numéricos válidos.")

# Executar o programa
main()
