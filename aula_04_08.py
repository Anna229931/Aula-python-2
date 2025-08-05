#listas
carros = []
print(carros)
print(len(carros))

carros = ["Accord", "Polo", "Civic", "Fiat uno"]
print(carros)
print(len(carros))
print(carros[1])
carros[0] = "Jetta"
print(carros[0])
carros_back = carros
carros_back = carros[:] #fatiamento :
print(carros_back)
carros[3] = "Jeep"
print(carros)
print(carros_back)
print(carros_back[-2])
print(carros_back[:3])

# notas = [6, 7, 5, 8, 9]
# soma = 0
# x = 0
# while x < len(notas):
#     soma += notas[x]
#     x += 1
# print(f"Média = {(soma/x):.2f}")
# notas = [0,0,0,0,0]
# soma = 0
# x = 0
# while x < len(notas):
#     notas[x] = float(input(f"Nota{x+1} = "))
#     soma += notas[x]
#     x += 1
# print(f"Média = {(soma/x):.2f}")

#Exercício 1 Escreva um programa para ler 7 notas e calcular a média aritmética.
# notas = [0,0,0,0,0,0,0]
# soma = 0
# x = 0
# while x < 7:
#     notas[x] = float(input(f""))



