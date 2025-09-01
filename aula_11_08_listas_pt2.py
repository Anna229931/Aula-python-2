#append - listas
# nomes_alunos = []
# print(len(nomes_alunos))
# nomes_alunos.append("Lunna")
# print(nomes_alunos)
# nomes_alunos.append("Letícia")
# print(nomes_alunos)
# nomes_alunos.append("Anna")
# print(nomes_alunos)
#
# nomes_alunos.sort()
# print(nomes_alunos)
# nomes_alunos.sort(reverse=True)
# print(nomes_alunos)
#
# 1. Vejamos um programa que lê números até que 0 (zero) seja
# digitado, depois o programa imprimirá na mesma ordem em que foram digitados:
# nomes_alunos = []
# while True:
#     nome = input("digite um nome (digite fim para sair):  ")
#     if nome == "fim":
#         break
#     nomes_alunos.append(nome)
#     nomes_alunos.sort()
# x = 0
# while x < len(nomes_alunos):
#     print(nomes_alunos[x])
#     x+=1

# nome_alunos2 = []
# nome_alunos2.extend(['Anna', 'Lunna'])
# print(nome_alunos2)
# nome_alunos2.extend(["Lucas", "Flávio"])
# print(nome_alunos2)
# nome_alunos2.append(["Diana"])
# print(nome_alunos2)

#2. Faça um programa que leia duas listas e que gere uma terceira com os elementos
# das duas primeiras.
lista_alunos = ["Anna", "Lunna", "Michele", "Letícia"]
nova_lista_alunos = []
while True:
    novo_aluno = input("Nome (enter para sair): ")
    if novo_aluno == "":
        break
    nova_lista_alunos.append(novo_aluno)

#atualização_lista_alunos = lista_alunos + nova_lista_alunos
atualização_lista_alunos = []
atualização_lista_alunos.extend(lista_alunos + nova_lista_alunos)
atualização_lista_alunos.sort()
print(atualização_lista_alunos)
