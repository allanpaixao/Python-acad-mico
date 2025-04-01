nome=input("Digite o nome")
idade=int(input("Digite a sua idade"))
altura=float(input("Digite a altura (em metros):"))
peso=float(input("Digite o peso(em kg): "))
imc=peso/(altura**2)
if imc<18.5:
           Classificacao="Abaixo do peso"
elif imc<24.9:
           classificacao="peso normal"
elif imc<29.9:
           classificacao="sobrepeso"
elif imc <34.9:
           classificacao="obesidade grau 1"
elif imc<39.9:
           classificacao="obesidade grau 2"
else:
           classificacao="obesidade grau 3"
print(f"NOME: {nome}")
print(f"IDADE: {idade}anos")
print(f"Altura: {altura:.2f}m")
print(f"Peso: {peso:.2f}kg")
print(f"IMC: {imc:.2f}")
print(f"Classificação:{classificacao}")
