def calcular_imc(peso, altura):
    imc = peso / (altura ** 2)
    return imc

peso = float(input("Digite seu peso (kg): "))
altura = float(input("Digite sua altura (m): "))

imc = calcular_imc(peso, altura)
print(f"Seu IMC é: {imc:.2f}")

if imc < 45.0:
    print("Classificação: Abaixo do peso")
elif 45.0 <= imc < 50.0:
    print("Classificação: Peso normal")
elif 50.0 <= imc < 60.0:
    print("Classificação: Sobrepeso")
elif 60.0 <= imc < 80.0:
    print("Classificação: Obesidade Grau I")
elif 80.0 <= imc < 120.0:
    print("Classificação: Obesidade Grau II")
else:
    print("Classificação: Obesidade Grau III (mórbida)")
