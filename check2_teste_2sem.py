#Uma empresa de tecnologia contratou um grupo de estudantes 
# para desenvolver um sistema em Python que registre o 
# desempenho de alunos em diferentes disciplinas e calcule 
# sua média final, utilizando listas, laços de repetição e dicionários.
#Cada aluno deve ter suas notas organizadas por semestre, e 
# cada semestre deve conter as seguintes avaliações:
#•	3 Checkpoints
#•	2 Sprints
#•	1 Global Solution (GS)
#4.	O programa deve armazenar os dados de cada aluno em um dicionário, onde:
#o	A chave é o nome do aluno.
#o	O valor é outro dicionário contendo as notas e médias calculadas.
#Exemplo:
#alunos = {
#    "Ana": {"1º Semestre": 8.0, "2º Semestre": 9.2, "Média Final": 8.8},
#    "Carlos": {"1º Semestre": 7.5, "2º Semestre": 8.0, "Média Final": 7.8}
#}

#🚩 Tarefas
#Implemente em Python um programa que:
#1.	Solicite ao usuário quantos alunos serão cadastrados.
#2.	Para cada aluno:
#o	Peça o nome e as notas dos dois semestres.
#o	Armazene as notas de cada semestre em listas.
#o	Calcule as médias conforme as fórmulas acima.
#o	Armazene os resultados em um dicionário principal.
#3.	Após o cadastro, exiba todas as médias finais, indicando se o 
# aluno foi Aprovado (≥6.0) ou Reprovado (<6.0).
#4.	Utilize pelo menos uma estrutura for e uma estrutura while em seu código.

#🍀 Desafio (+1 ponto extra)
#Inclua uma função chamada resumo_turma() que, usando o dicionário principal:
#•	Mostre o número total de alunos cadastrados;
#•	Calcule e exiba a média geral da turma;
#•	Mostre o nome e a média do melhor aluno.

# -----------------------------------------------------

# dicionário principal para armazenar os alunos e suas médias
alunos = {}

# Solicita a quantidade de alunos a serem cadastrados
qtd_alunos = int(input("Quantos alunos deseja cadastrar? "))

# Estrutura de repetição para o cadastro de cada aluno
for i in range(qtd_alunos):
    nome = input(f"\nDigite o nome do aluno {i+1}: ").lower()

    # Dicionário interno para armazenar dados do aluno
    dados = {}

    # Repetição dos 2 semestres
    semestre = 1
    while semestre <= 2:
        print(f"\n--- {semestre}º Semestre ---")

        # Leitura das 3 notas de checkpoint
        cps = []
        for j in range(3):
            nota_cp = float(input(f"Checkpoint {j+1}: "))
            if nota_cp < 0 or nota_cp > 10:
                print("Nota inválida! Digite uma nota entre 0 e 10.")
            elif nota_cp >= 0 and nota_cp <= 10:
                cps.append(nota_cp)

        # Descarta a menor nota
        cps.remove(min(cps))

        # Leitura das notas de sprint e GS
        sprints = []
        for s in range(2):
            nota_sprint = float(input(f"Sprint {s+1}: "))
            if nota_sprint < 0 or nota_sprint > 10:
                print("Nota inválida! Digite uma nota entre 0 e 10.")
            elif nota_sprint >= 0 and nota_sprint <= 10:
                sprints.append(nota_sprint)

        gs = float(input("Global Solution (GS): "))
        if gs < 0 or gs > 10:
            print("Nota inválida! Digite uma nota entre 0 e 10.")
        elif gs >= 0 and gs <= 10:
            pass

        # Cálculo da média semestral
        media_semestre = (((sum(cps) + sum(sprints)) / 4) * 0.4) + (gs * 0.6)

        # Armazena no dicionário interno
        dados[f"{semestre}º Semestre"] = round(media_semestre, 1)

        semestre += 1  # incrementa o contador do while

    # Cálculo da média final
    media_final = (dados["1º Semestre"] * 0.4) + (dados["2º Semestre"] * 0.6)
    dados["Média Final"] = round(media_final, 1)

    # Adiciona o aluno e seus dados no dicionário principal
    alunos[nome] = dados

# -----------------------------------------------------
# Exibição dos resultados e situação de cada aluno
# -----------------------------------------------------
print("\n=== RESULTADOS FINAIS ===")
for nome, dados in alunos.items():
    situacao = "Aprovado" if dados["Média Final"] >= 6 else "Reprovado"
    print(f"\nAluno: {nome}")
    print(f"  1º Semestre: {dados['1º Semestre']}")
    print(f"  2º Semestre: {dados['2º Semestre']}")
    print(f"  Média Final: {dados['Média Final']} - {situacao}")

# -----------------------------------------------------
# 🍀 Desafio: resumo_turma()
# -----------------------------------------------------
def resumo_turma(dicionario):
    total = len(dicionario)
    soma_medias = 0
    melhor_aluno = ""
    maior_media = 0

    # percorre o dicionário de alunos
    for nome, dados in dicionario.items():
        soma_medias += dados["Média Final"]
        if dados["Média Final"] > maior_media:
            maior_media = dados["Média Final"]
            melhor_aluno = nome

    media_turma = soma_medias / total

    print("\n=== RESUMO DA TURMA ===")
    print(f"Total de alunos: {total}")
    print(f"Média geral da turma: {media_turma:.1f}")
    print(f"Melhor aluno: {melhor_aluno} (Média {maior_media})")

# Chamada da função extra
resumo_turma(alunos)