print("********************")
print("Nota do aluno")
print("*******************")

nome=input("Digite o nome do Aluno: ")
av1=float(input("Digite a primeira nota do aluno: "))
av2=float(input("Digite a segunda nota do aluno: "))
media=(av1+av2)/2
if(media>=6):
    print(f" O aluno {nome} está aprovado com media {media:.1f}")
elif(media>=4.0):
       print(f"O aluno {nome} está em exame final com media igual a {media:.2f}")
else:
        print(f" O aluno {nome} está reprovado com media {media:.1f}")
