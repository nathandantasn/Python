print("\nOlá, descubra qual é seu peso ideal, através de duas informações básicas!")

sexo = str(input("\nDigite seu sexo(Feminino ou Masculino): "))
sexo = sexo.upper()

while sexo != "FEMININO" and sexo !="MASCULINO":
    print("Sexo digitado não é válido!")
    sexo = str(input("Digite seu sexo(Feminino ou Masculino): "))
sexo = sexo.upper()

altura = float(input("\nDigite sua altura(Ex: 1.69): "))

if sexo == "MASCULINO":
    print("\nSeu peso ideal é: %.3f Kg" %(altura*72.7 - 58.0)) 

else:
    print("\nSeu peso ideal é: %.3f Kg" %(altura*62.1 - 44.7))
