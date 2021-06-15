saque = float(input("Digite o valor que deseja sacar (entre R$10 e R$600): ").replace(",","."))

while saque < 10 or saque > 600:
    saque = float(input("Digite o valor que deseja sacar (entre R$10 e R$600): ").replace(",","."))
else:
    print(f"\nValor de saque liberado R$ {int(saque)}")
    cem = int(saque//100)
    saque = saque % 100

    cinquenta = int(saque//50)
    saque = saque % 50

    dez = int(saque//10)
    saque = saque % 10

    cinco = int(saque//5)
    saque = saque % 5

    um = int(saque//1)
    saque = saque % 1

print("\nSerão fornecidas:")

print(f"{um} notas de R$ 1,00")
print(f"{cinco} notas de R$ 5,00")
print(f"{dez} notas de R$ 10,00")
print(f"{cinquenta} notas de R$ 50,00")
print(f"{cem} notas de R$ 100,00")