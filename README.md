# Projeto Git/Github

## O que é Git?

Em termos simples, o Git permite que você mantenha um histórico de alterações
 em seu código, facilitando a colaboração em equipe e o gerenciamento de projetos.
 Cada contribuição é registrada como um "commit", que contém uma descrição da alteração e uma referência única (hash).


## O que é Github?

GitHub, por outro lado, é uma plataforma de hospedagem de código que utiliza o Git.


## Relacionamento entre Git & Github

1. **Hospedagem de Repositórios**

2. **Colaboração em Equipe** 

3. **Rastreamento de Problemas e Projetos**

4. **Forks e Branches**

5. **Versionamento de Código** 

## Objetivos

- Listar e aprender comandos básicos do Git

- Usar os produtos Git/Github

- Aprender como colaborar em equipe no projeto

# GIT: Configurações e comandos principais

## Configuração 

- Configuração básica para autenticação de usuário e e-mail
**É recomendado usar o mesmo usuário e e-mail do Github**

`git config --global user.name "nome-usuario"` <br><br>
`git config --global user.email "email"`

- Mudar branch padrão para *main*

`git config --global init.defaultBranch main`

- Configuração para salvar credenciais

`git config --global credential.helper store`

__Essa configuração habilita as credencais como um token <br> de autenticação ficarem salvas permanentemnte__

`git config --global credential.helper cache`

__Essa configuração permite que as credenciais como um token fiquem salvas até 15 minutos__

## Comandos Principais


### Fazer um clone do codigo-fonte

`git clone https://github.com/louis0113/Projeto-Git.git`

### Salvar mudanças

`git add .`

### Salvar commit com mensagem

`git commit -m "v0.1"`

### Adicionar git remota

`git remote add origin`

### Mandar mudanças para o repositorio remoto

`git push origin main`

### Atualizar repositório local

`git pull origin main` 

# IA do Github para escrever códigos Python :)

- Algoritmos a se fazer:

    - [x] Concatenando Dados: Dar dois inputs de strings e o output ser a concatenação dessas strings

    - [x] Repetindo Textos: Input de um inteiro e uma string, o inteiro vai ser a quantidade de vezes da repetição da String no output

    - [x] Operações Matemáticas: Input de dois números e realizar as quatro operações

    - [x]  Verificação Par e Impar: Input de um numero e fazer a verificação se é par ou ímpar

    - [x] Média de Notas: Calcular a média aritmética de três notas 

    - [x] Verificar Palíndromos: Inverter uma string e comparar se continua sendo a palavra anterior
## Criação do site

### Items básicos de um site estático

**SRC**
- (Pronunciado 'Source') Pasta usada para armazenar arquivos HTML.

**CSS**
- Pasta para armazenar arquivos de Style Sheet Language (CSS).

**ASSETS**
- Pasta para armazenar aquivos de mídia.
