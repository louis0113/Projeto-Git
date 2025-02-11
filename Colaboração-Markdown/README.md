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

## Ciclo de vida de mudanças no codigo com GIT


## Fazer um clone do codigo-fonte

`git clone https://github.com/louis0113/Projeto-Git.git`

## Salvar mudanças

`git add .`

## Salvar commit com mensagem

`git commit -m "v0.1"`

## Adicionar git remota

`git remote add origin`

## Mandar mudanças para o repositorio remoto

`git push origin main`

## Atualizar repositório local

`git pull origin main` 

