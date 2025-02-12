print('Por favor digite dois numeros para as operações basicas, nota o primeiro número será o \033[32mdividendo\033[m,')
print('e o segundo será o \033[32mdivisor\033[m.')

n = float(input('Digite um número: '))
n2 = float(input('Digite um segundo número: '))

s = n + n2

if n > n2:
    d = n - n2
else:
    d = n2 - n

p = n * n2

div = n / n2

print('A soma será de \033[32m{}\033[m, a diferença \033[32m{}\033[m, o produto \033[32m{}\033[m e a divisão \033[32m{:.1f}\033[m'.format(s,d,p,div))