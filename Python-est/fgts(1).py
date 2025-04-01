print("********************")
print("Recolhimento do FGTS")
print("*******************")

nome=input("Digite o nome do contribuinte: ")
cpf = int(input("Digite o cpf do contribuinte: "))
salario=float(input("Qual o salario do contribuente: "))
fgts=salario*0.08
print(f"Nome: {nome}")
print(f"Cpf: {cpf}")
print(f"Recolhimento do FGTS: {fgts:.2f}")

