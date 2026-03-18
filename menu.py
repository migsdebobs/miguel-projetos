def calcular():

    while True :

        print("1 = soma")
        print("2 = subtra")
        print("3 = divisao")
        print("4 = vezes")

        numero1 = int(input("Digite o primeiro número: "))
        numero2 = int(input("Digite o segundo número: "))

    
        opcao = int(input("Digite sua operação: "))

        if opcao  == 1:

            print(f"{numero1+numero2}")

        elif opcao  == 2:

            print(f"{numero1-numero2}")

        elif opcao  == 3:

            print(f"{numero1/numero2}")

        elif opcao  == 4:

            print(f"{numero1*numero2}")
        
        else: 
         
            break


calcular()