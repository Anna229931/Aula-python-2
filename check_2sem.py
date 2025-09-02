notas_semestre1 = ()
notas_semestre2 = ()

for sem in range(1, 3):
    print(f"\nSemestre {sem}:")

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
    media_semestral = (media_check_sprint * 0.4) + (gs * 0.6)

    if sem == 1:
        media_sem1 = media_semestral*0.4
        notas_semestre1 = media_sem1
    if sem == 2:
        media_sem2 = media_semestral*0.6
        notas_semestre2 = media_sem2



print("\n--- Resultados ---")

print(f"Média final = {notas_semestre1 + notas_semestre2:.1f}")
