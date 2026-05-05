
quantidade = 3 
lista_empresa = []

def chamar_função():

    for i in range(quantidade):
        nome = input(f"fale nome da empresa:  {i+1} ")
    
        print(f"{nome}")
        lista_empresa.append(nome)

    print (f"esta aqui usa lista de empresa {lista_empresa}")
    return

chamar_função()