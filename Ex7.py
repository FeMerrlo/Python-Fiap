from re import T


P =float (input ('Digite o valor:  '))
A =float (input ('Digite o valor:  '))
B =float (input ('Digite o valor:  '))
C =float (input ('Digite o valor:  '))
D =float (input ('Digite o valor:  '))

TP = P+A+B+C+D
print ("Valor da compra", TP)
PG =float (input ('Insira total a pagar: '))
T = PG-TP
print("Valor do troco R$  ", T)
