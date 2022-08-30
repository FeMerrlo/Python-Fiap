
Peso = float(input("Digite a peso: "))

Sexo = input("Digite o sexo (M/F): ")

Altura = float(input("Digite a altura: "))
IMC = Peso/(Altura*Altura)
if (Sexo == "M"):
    if(IMC>25):
        print ("Acima")
    elif(IMC<20):
        print ("Abaixo")
    else:
        print ("Normal")
if (Sexo == "F"):
    if(IMC>25):
        print ("Acima")
    elif(IMC<20):
        print ("Abaixo")
    else:
        print ("Normal")      