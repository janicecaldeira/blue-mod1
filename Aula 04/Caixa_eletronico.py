saque = float(input("Qual o valor você deseja sacar (entre R$10 e R$600): ").replace(",","."))

while saque < 10 or saque > 600:
    saque = float(input("Por favor, informe um valor entre R$10 e R$600: ").replace(",","."))
else:
    print(f"\n\U0001F4A1 Valor de saque liberado: R$ {int(saque)}")
    cem = saque//100
    saque = saque % 100

    cinquenta = saque//50
    saque = saque % 50

    dez = saque//10
    saque = saque % 10

    cinco = saque//5
    saque = saque % 5

    um = saque//1
    saque = saque % 1

print("\nSerão fornecidas:")

if cem > 0:
    print(f"\U0001F4B2 {int(cem)} nota(s) de R$ 100,00")

if cinquenta > 0:
    print(f"\U0001F4B2 {int(cinquenta)} nota(s) de R$ 50,00")

if dez > 0:
    print(f"\U0001F4B2 {int(dez)} nota(s) de R$ 10,00")

if cinco > 0:
    print(f"\U0001F4B2 {int(cinco)} nota(s) de R$ 5,00")

if um > 0:
    print(f"\U0001F4B2 {int(um)} nota(s) de R$ 1,00")