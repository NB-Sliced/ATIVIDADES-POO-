#pede coordenadas ao usuario
a = int(input("digite a cordenada x do ponto 1:"))
b = int(input("digite a cordenada y do ponto 1:"))
c = int(input("digite a cordenada x do ponto 2:"))
d = int(input("digite a cordenada y do ponto 2:"))
e = int(input("digite a cordenada x do ponto 3:"))
f = int(input("digite a cordenada y do ponto 3:"))
g = int(input("digite a cordenada x do ponto 4:"))
h = int(input("digite a cordenada y do ponto 4:"))


#calcular o tamanho dos lados
formula12= ((a - c)**2 + (b - d)**2)
formula23= ((c - e)**2 + (d - f)**2)
formula34= ((e - g)**2 + (f - h)**2)
formula41= ((a - g)**2 + (b - h)**2)

#calcular o tamanho das diagonais
diag13 = (a - e)**2 + (b - f)**2
diag24 = (c - g)**2 + (d - h)**2

print(f"Distancia do ponto 1 e 2 é igual a {formula12} ")
print(f"Distancia do ponto 2 e 3 é igual a {formula23} ")
print(f"Distancia do ponto 3 e 4 é igual a {formula34} ")
print(f"Distancia do ponto 4 e 1 é igual a {formula41} ")
print()
print(f"o valor das Diagonais é igual a 1-3: {diag13}")
print(f"o valor das Diagonais é iguala  2-4: {diag24}")
tama = [formula12, formula23, formula34, formula41]

#armazena a quantidade de lados e diagonais
lado = 0
diagonal = 0


#ajuda a definir quem é o lado e as diagonais
minimo = min(tama)
maximo = max(tama)

for t in tama:
    if t == minimo:
       lado += 1
    elif t == maximo:
       diagonal += 1


#eps ajuda que aconteca erros por milidecimos de diferença
EPS = 1e-6

# verifica seé um quadrado
if (abs(formula12 - formula23) < EPS and
    abs(formula23 - formula34) < EPS and
    abs(formula34 - formula41) < EPS and
    abs(diag13 - diag24) < EPS and
    formula12 > 0):
    print("teos um quadrado")

# verifica se temos retângulo
elif abs(formula12 - formula34) < EPS and abs(formula23 - formula41) < EPS and abs(diag13 - diag24) < EPS:
    print("temos um retângulo")

# quadrilátero irregular
elif formula12 != formula23 and formula23 != formula34 and formula41 != formula12:
    print("isso é um quadrilátero irregular")



