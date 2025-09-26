print("sugestões das coordenadas dos tipos de triangulos")
print()
print(" 0 ou qualquer outro numero = ir sem sugestões")
print(" 1 = Equilatero")
print(" 2 = Isosceles")
print(" 3 = Escalendo")
print()

escolha = int(input("qual tipo você deseja ??? digite o número correspondente:"))

if escolha == 1:
    print("[0,0] [2,0] [1,1.732050801]")
elif escolha == 2:
    print("[0,0] [4,0] [2,3]")
elif escolha == 3:
    print("[0,0] [4,0] [3,2]")
elif escolha == 0:
    print("divirtasse")
else:
    print("vá sem sugestão")

#pede pontos para o usuario
a = float(input("digite a cordenada x do ponto 1:"))
b = float(input("digite a cordenada y do ponto 1:"))
c = float(input("digite a cordenada x do ponto 2:"))
d = float(input("digite a cordenada y do ponto 2:"))
e = float(input("digite a cordenada x do ponto 3:"))
f = float(input("digite a cordenada y do ponto 3:"))


#printa as cordenadas escolhidas
print(f" CORDENADAS ( X / Y ) ")
print(f" PONTO 1 CORDENADAS ({a},{b}) ")
print(f" PONTO 2 CORDENADAS ({c},{d}) ")
print(f" PONTO 3 CORDENADAS ({e},{f}) ")

#calcula o tamanho dos lados
formula12= ((a - c)**2 + (b - d)**2)**0.5
formula23= ((c - e)**2 + (d - f)**2)**0.5
formula31= ((a - e)**2 + (b - f)**2)**0.5

print(f"Distancia do ponto 1 e 2 é igual a {formula12:.2} ")
print(f"Distancia do ponto 2 e 3 é igual a {formula23:.2} ")
print(f"Distancia do ponto 3 e 1 é igual a {formula31:.2} ")

#evitar que 3 pontos na mesma reta resultem em algum tipo de triangulo
area = abs(a*(d - f) + c*(f - b) + e*(b - d)) / 2
if area == 0:
    print("não é um triangulo")

else:
    #evitar , serve para tirar a chance de erros muitoo pequenos
    evitar = 1e-6
    #armazena a comparação dos tamanhos
    mermo_tamanho = 0

    if abs(formula12 - formula23) < evitar:
        mermo_tamanho += 1
    if abs(formula12 - formula31) < evitar:
        mermo_tamanho += 1
    if abs(formula23 - formula31) < evitar:
        mermo_tamanho += 1
    #printa o tipo de triangulo com base nas informações coletadas
    if mermo_tamanho == 3:
        print("o triangulo é equilatero")
    elif mermo_tamanho >=1:
        print("é um triangulo isosceles")
    else:
        print("é um triangulo escalendo")