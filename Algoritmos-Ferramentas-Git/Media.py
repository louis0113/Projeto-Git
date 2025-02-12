print('Calculo de media do aluno universitario, nota, a primeira nota será multiplicada por \033[32m2\033[m], e a segunda por \033[32m3\033[m,')
print('e a divisão será por \033[32m5\033[m')

n = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))

m = (n*2 + n2*3)/5

x = ''

if m >= 7:
    x = '\033[32mfoi aprovado\033[m'
elif 3 < m < 7:
    x = '\033[33mfoi para a recuperação\033[m'
else:
    x = '\033[31mfoi reprovado\033[m'

print('O aluno {}, com a media {:.1f}'.format(x,m))