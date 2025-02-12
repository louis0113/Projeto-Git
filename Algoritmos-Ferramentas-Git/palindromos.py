# Faça o input de uma string, revertendo a string e verificando se a string é um palíndromo.

string1 = input("Digite uma string: ")

if string1 == string1[::-1]:
    print("\nA string é um palíndromo.")
else:
    print("\nA string não é um palíndromo.")