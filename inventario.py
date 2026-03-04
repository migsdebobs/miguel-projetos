trans = [100.50,-20.00,50.00,-150.00,300.00]

total_positivo = 0

for valor in trans:
    if valor < 0:
        total_positivo += valor

print(f"total de depositos : R$ {total_positivo}")