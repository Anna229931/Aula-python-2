# Nomes do grupo: ___________________________

qtd_alunos = int(input("Quantidade de alunos: "))

medias_turma = []  # lista para armazenar médias de todos os alunos

for i in range(1, qtd_alunos + 1):
    print(f"\nAluno {i}:")
    
    # leitura dos checkpoints
    cps = []
    n = 1
    while n <= 3:
        nota = float(input(f"Checkpoint {n} (0 a 10): "))
        cps.append(nota)
        n += 1
    
    # descartar a menor nota
    menor_cp = min(cps)
    cps.remove(menor_cp)
    
    # leitura das sprints
    sprints = []
    n = 1
    while n <= 2:
        nota = float(input(f"Sprint {n} (0 a 10): "))
        sprints.append(nota)
        n += 1
    
    # leitura da GS
    gs = float(input("Global Solution (0 a 10): "))
    
    # cálculo da média
    media_check_sprint = (sum(cps) + sum(sprints)) / 4
    media_final = (media_check_sprint * 0.4) + (gs * 0.6)
    medias_turma.append(media_final)
    
    # saída individual
    print(f"CPs (com menor descartado): {cps}")
    print(f"Sprints: {sprints}")
    print(f"GS: {gs}")
    print(f"Média final = {media_final:.1f}")
    
    if media_final >= 6:
        print("Situação: Aprovado")
    else:
        print("Situação: Reprovado")

# resumo da turma
print("\n--- Resultados da Turma ---")
media_geral = sum(medias_turma) / len(medias_turma)
print(f"Média geral = {media_geral:.1f}")
print(f"Maior média = {max(medias_turma):.1f}")
print(f"Menor média = {min(medias_turma):.1f}")
