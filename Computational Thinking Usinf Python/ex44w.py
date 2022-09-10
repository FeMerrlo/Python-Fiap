from ast import Continue


N = float(input("Digite um valor N: "))
while (N < 0):
     print("Não será permitido valor negativo")
     N = float(input("Entre com um valor N: "))
     continue

