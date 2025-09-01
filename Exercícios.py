# 1) A lista de temperaturas de Mons, na Bélgica, foi 
#armazenada na lista T = [-10, -8, 0, 1, 2, 5, -2, -4]. Faça
#um programa que imprima a menor e a maior
#temperatura, assim como a temperatura média 

#T = [-10, -8, 0, 1, 2, 5, -2, -4]
#temp_media = sum(T) / len(T)
#print(f"Temperatura máxima: {max(T)}, Temperatura mínima: {min(T)}, Temperatura média: {temp_media}")

#2) 
"1" == 5.00
"2" == 3.50
"3" == 10.00
"5" == 4.75
"9" == 8.90
codigo = []
quantidade = []
valores = []
while True:
    cod = input("Código do produto (0 para sair): ")
    if cod == "0":
        break
    codigo.append(cod)
    qtd = int(input("Quantidade: "))
    quantidade.append(qtd)
    if cod == "1":
        valores.append(5.00 * qtd)
    elif cod == "2":
        valores.append(3.50 * qtd)
    elif cod == "3":
        valores.append(10.00 * qtd)
    elif cod == "5":
        valores.append(4.75 * qtd)
    elif cod == "9":
        valores.append(8.90 * qtd)
    else:
        print("Código inválido")
        codigo.pop()
        quantidade.pop()
for i in range(len(codigo)):
    print(f"Código: {codigo[i]} \n Quantidade: {quantidade[i]} \n Valor: R${valores[i]:.2f}\n")
print(f"Total da compra: R${sum(valores):.2f} \n Média dos preços: R${sum(valores)/len(valores):.2f} \n Valor máximo: R${max(valores):.2f} \n Valor mínimo: R${min(valores):.2f}")
