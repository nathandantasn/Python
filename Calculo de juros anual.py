#Calculo de juros anual

cod = 2
while cod == 2:
    investiment = float(input("\nDigite o valor a ser investido: R$ "))
    percentage = float(input("Digite o juros mensal: % "))
    cod = 0
    year = 0
    balance = 0
    interest = 0
    while cod == 0:
        i = 1
        year+=1
        while i < 13:
            interest = (balance + investiment) * percentage
            balance = balance + investiment + interest
            investiment = 0

            print("%iº mês, o valor será R$ %.2f" %(i, balance))
            i+=1

        print("\nApós um ano de investimento, o valor será R$ %.2f" %(balance))
        print("\nDeseja calcular mais um ano, começar de novo ou encerrar o aplicativo?")
        cod = int(input("Digite 0 para continuar, 1 para encerrar e 2 para começar de novo "))
        print("\nApós %i ano(s) seu saldo será R$ %.2f\n" %(year,balance))
