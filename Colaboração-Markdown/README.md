# GIT: Configurações e comandos principais

## Configuração 

Configuração básica para autenticação de usuário e e-mail
**É recomendado usar o mesmo usuário e e-mail do Github**

`git config --global user.name "nome-usuario"` <br><br>
`git config --global user.email "email"`

Mudar branch padrão para *main*

`git config --global init.defaultBranch main`

Configuração para salvar credenciais

`git config --global credential.helper store`

__Essa configuração habilita as credencais como um token <br> de autenticação ficarem salvas permanentemnte__

`git config --global credential.helper cache`

__Essa configuração permite que as credenciais como um token fiquem salvas até 15 minutos__

## Comandos Principais

## Olá Mundo(começar apagar por aqui)

__Estou livre da maldição__

__Certo e agora?__
```
n = float(input('Digite uma nota: '))
n2 = float(input('Digite outra nota: '))

media = (n + n2)/2

print('A media foi {}'.format(media))
```
