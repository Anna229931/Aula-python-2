# a = int(input("Primeiro valor: "))
# b = int(input("Segundo valor: "))
# if a > b:
#     print("O primeiro valor é maior!")
# else:
#     print("o segundo é maior!")
print()
#exercício 1
# velocidade = float(input("Velocidade inicial em km/h = "))
# limite_de_velocidade = 80
# if velocidade > limite_de_velocidade:
#     excesso = velocidade - limite_de_velocidade
#     multa = 5*excesso
#     print("a multa é de = ", multa)
# else:
#     print("sem multa")
print()
#exercício 2
# a = int(input("A = "))
# b = int(input("B = "))
# c = int(input("C = "))
# maior = max(a, b, c)
# menor = min(a, b, c)
# print("o maior númeo é =", maior)
# print("o menor número é", menor)
# #Exercício 4
# distancia = float(input("distancia que deseja percorrer"))
# if distancia <= 200:
#     preco1 = 0.50 * distancia
#     print("o preco é R$", preco1)
# else:
#     preco2 = 0.45 * distancia
#     print("o preco é R$",preco2)
#Exercício 5
# num1 = float(input("número 1:"))
# num2 = float(input("número 2:"))
# operação = int(input("digite a operação que quer realizar:\n 1 - subtração, 2 - adição, 3 - multiplicação, 4 - divisão"))
# if operação == 1:
#     sub = num1 - num2
#     print("%2f"%sub)
# elif operação == 2:
#     soma = num1 + num2
#     print("%2f"%soma)
# elif operação == 3:
#     mul = num1 * num2
#     print("%2f"%mul)
# elif operação == 4:
#     div = num1/num2
#     print("%.2f"%div)
# Exercicio 6
valor_casa = float(input("valor da casa:"))
salario = float(input("seu salário:"))
anos = int(input("quantos anos irá pagar:"))
prestação = valor_casa/(anos * 12)
if anos <= salario*0.3:
    print("A prestação é:",prestação)
else:
    print("prestação negada")




