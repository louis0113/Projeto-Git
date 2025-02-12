print('Vamos determinar se um número é par ou impar.')

n = int(input('Digite um número inteiro: '))

if n%2 == 0:
    print('O \033[32m{}\033[m é um número par.'.format(n))
else:
    print('O \033[32m{}\033[m é um número impar.'.format(n))