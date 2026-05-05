def fazer_camisa():

    tamanho = input("qual tamanho da sua camisa : ")
    modelo =  input("qual modelo da sua camisa : ")

    total = tamanho, modelo


    if tamanho == "M" and modelo == "Boxy":

        print(f"jovem{total}")

    elif tamanho == "P"  :
        print(f"Bebezao{total}")

    elif tamanho == "G"  :
        print("gordo")

fazer_camisa()