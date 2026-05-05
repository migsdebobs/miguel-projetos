saldo_inicial = 1000.00

while True:
    print("\n--- MENU ---")
    print("1 - Ver Saldo")
    print("2 - depositar")
    print("3 - sacar") 
    print("4 - Sair")
    
    
    escolha = input("Digite a opção desejada: ") 
    if escolha == "1":
        print(f"Seu saldo atual é: R$ {saldo_inicial:.2f}")
    elif escolha == "4":
        print("Saindo do sistema...")
        
    elif escolha == "2":
        valor_de_depositar = float(input("quantos voce quer depositar : "))
        saldo_inicial += valor_de_depositar

        print (f"seu valor depositado {saldo_inicial}")

    elif escolha == "3":
        valor_saque = float(input("Quanto você deseja sacar: "))
        
        if valor_saque <= 0:
            print("[ERRO] Valor de saque deve ser maior que zero.")
            
        elif valor_saque > saldo_inicial:
            print(f"Saldo insuficiente! Seu saldo atual é R$ {saldo_inicial:.2f}")
            
        else:  
            # Atualiza o saldo real da conta
            saldo_inicial -= valor_saque 
            print(f"Saque realizado: R$ {valor_saque:.2f}")
            print(f"Saldo atualizado: R$ {saldo_inicial:.2f}")
        
    elif escolha == "4":
        print("sair desse sistema")
        break
            