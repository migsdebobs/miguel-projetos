
while True:
    try:
        numero1 = float(input("digite um numero :"))
        numero2 = float(input("digite um numero :"))


        resultado = numero1/numero2
    

        print(f"este e o valor da divisao: {resultado}")
        break
    except ValueError :

        
        print("invalido tente de novo")
    except ZeroDivisionError:
        print("nao e possivel por zero")
    