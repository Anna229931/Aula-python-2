 #Dicionario é composto por um conjunto de chaves e valores (CPF) uma chave e varios valores
# alunos_fiap = {"565560": ["Anna","1ECR"], "564040":["Leticia","1EMR"]}
# alunos_fiap["564040"][1] = "1ECR" #para mudar algum erro, vc coloca a chave o indice e pah
# print(alunos_fiap["564040"])
# print("565560" in alunos_fiap) #verificar se ta dentro do bagui
# print("565561" in alunos_fiap)
# nomes_alunos = ["Anna", "Leticia"]
# print("Ana" in nomes_alunos) #Serve pra pesquisar dentro da chave tbm
# print(alunos_fiap.keys()) #As chaves que possuem dentro do seu dicionario
# print(alunos_fiap.values()) #Mostra os valores
#pode usar del também igual em lista tipo del alunos_fiap["565560"]
# cursos_fiap = {"Administração": ["6K","3 anos"], "Mecatrônica": ["3K","4 anos"], "Marketing": ["2k", "1 ano"]}
# while True:
#     pesquisa = input("Digite o curso ou fim para terminar:") #.lower() pra quando digitar de qualquer forma vai ficar td maiusculo ou minusc
#     if pesquisa == "fim":
#         break
#     if pesquisa in cursos_fiap:
#         print(f"Valor = {cursos_fiap[pesquisa][0]} // Tempo perdido = {cursos_fiap[pesquisa][1]}")
#     else:
#         print("Curso não encontrado")

#Tuplas
# lista_alunos = ["Guilherme", "Wallace", "Pedro"]
# print(lista_alunos)
#
# lista_alunos.extend("Michele", "Anna")
# print(lista_alunos)
#
# lista_alunos[0] = "Thiago"
# print(lista_alunos)

# tupla_alunos = ("Guilherme", "Wallace", "Pedro")
# print(tupla_alunos)
#
# aluno1, aluno2, aluno3 = tupla_alunos
# print(aluno1)

nota_check = ()
print(len(nota_check))


# nota_check = ("Michele",)
# print(len(nota_check)) #a vírgula faz considerar apenas a
# quantidade de elementos e não a quantidade de caracteres
# print(type(nota_check))
#
# nota_check = ("Michele",)
# print(len(nota_check))
# print(type(nota_check))

# lista_notas = [9, 10, 5, 8]
# print(lista_notas)
#
# tupla_notas = tuple(lista_notas)
# print(lista_notas)

notas_check1 = (6,8,4,10)
notas_check2 = (10,5,7,9)
notas_checks = notas_check1 + notas_check2
print(notas_checks)
