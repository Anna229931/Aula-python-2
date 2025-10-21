
# from função2 import soma,mul,sub,divi
# num1 = float(input("numero 1 = "))
# num2 = float(input("numero 2 = "))
# print(f"soma = {soma(num1, num2)}")
# print(f"multiplicação = {mul(num1, num2)}")
# print(f"subtração = {sub(num1, num2)}")
# print(f"divisão = {divi(num1, num2)}")

# from funcao2 import *
# num1 = float(input("numero 1 = "))
# num2 = float(input("numero 2 = "))
# print(f"soma = {soma(num1, num2)}")
# print(f"multiplicação = {mul(num1, num2)}")
# print(f"subtração = {sub(num1, num2)}")
# print(f"divisão = {divi(num1, num2)}")


def ehpar(x):
    return x % 2 == 0
print(ehpar(2))
print(ehpar(3))

def par_ou_impar(x):
    if ehpar(x):
        return "par"
    else:
        return "ímpar"
print(par_ou_impar(2))
print(par_ou_impar(3))
