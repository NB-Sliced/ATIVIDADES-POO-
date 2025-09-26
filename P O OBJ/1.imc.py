a = float(input("digite seu peso "))
b = float(input("digite sua altura "))

c = b**2

d = a / c

print(f"{d:.3}")

if d > 0 and d < 18.5:
    print("abaixo do peso")

if d > 18.5 and d < 24.9:
    print("Saudável ")

if d > 25 and d < 29.9:
    print("peso em excesso")

if d > 30 and d < 34.9:
    print("obesidade grau 1")

if d > 35 and d < 39.9:
    print("obesidade grau 2")

if d > 40:
    print("obesidade grau 3")