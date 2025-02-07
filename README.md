# Projeto Git/Github

## Objetivos

- Listar e aprender comandos básicos do Git

- Usar os produtos Git/Github

- Aprender como colaborar em equipe no projeto

## Configuração 

Configuração básica para autenticação de usuário e e-mail
**É recomendado usar o mesmo usuário e e-mail do Github**

`git config --global user.name "nome-usuario"` <br>
`git config --global user.email "email"`

Mudar branch padrão para *main*

`git config --global init.defaultBranch main`

Configuração para salvar credenciais

`git config --global credential.helper store`

__Essa configuração habilita as credencais como um token <br> de autenticação ficarem salvas permanentemnte __

`git config --global credential.helper cache`

__Essa configuração permite que as credenciais como um token fiquem salvas até 15 minutos_

_
