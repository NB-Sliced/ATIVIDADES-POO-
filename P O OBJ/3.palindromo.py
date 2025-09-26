a = input("digite um numero de 5 digitos e veja se ele é palíndromo:")

b = a [::-1]
if b == a:
    print("é um palindromo")
else:
    print("não é um palindromo")