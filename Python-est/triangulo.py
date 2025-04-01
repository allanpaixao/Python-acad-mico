l1=int(input("Digite o primeiro lado do triângulo"))
l2=int(input("Digite o segundo lado do triângulo"))
l3=int(input("Digite o terceiro lado do triângulo"))
if(l1!=l2 and l2!=l3 and l1!=l3):
 print("escaleno")
elif(l1==l2 and l2==l3):
 print("equilatero")
else:
 print("isósceles")    
