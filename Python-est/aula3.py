print("********************")
print("Calculadora de IMC")
print("*******************")
print("/n")


nome=input("Qual nome do paciente: ")
idade = int(input("Qual o idade do paciente: "))
peso=float(input("Qual o peso do paciente: "))
altura = float(input("Qual altura do paciente: "))
imc=peso/(altura**2)
print(f"Nome: {nome}")
print(f"Idade: {idade}")
print(f"Peso: {peso}")
print(f"altura: {altura}")
print(f"IMC: {imc:.2f}")
