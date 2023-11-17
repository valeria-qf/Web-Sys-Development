# Projeto Matrícula.

Sistema de Matrícula Django

## Sobre o Projeto

Este é um projeto que foi desenvolvido para a disciplina de Programação para Internet, utilizando Django 4.2.2, uma poderosa framework de desenvolvimento web baseada em Python. O principal objetivo é criar um sistema de matrícula que permite a realização de várias operações CRUD (Create, Read, Update, Delete) para Aluno, Curso e Cidade.

## Recursos Utilizados

- Django 4.2.2
- Python 3.x
- SQLite
- HTML/CSS/Bootstrap

## Funcionalidades

- CRUD de Alunos
- CRUD de Cursos
- CRUD de Cidades

## Instalação

### Pré-requisitos

Certifique-se de ter Python e Django instalados em seu ambiente. Caso não tenha, siga as instruções em [Python](https://www.python.org/downloads/) e [Django](https://docs.djangoproject.com/en/4.2/topics/install/).

### Passos para instalação

1. Clone o repositório
```sh
git clone https://github.com/JefersonQueiroga/matricula.git
```
2. Entre na pasta do projeto
```sh
cd matricula
```
3. Crie um ambiente virtual
```sh
python -m venv venv
```
4. Ative o ambiente virtual
```sh
# Windows
venv\Scripts\activate

# Unix or MacOS
source venv/bin/activate
```
5. Instale as dependências do projeto
```sh
pip install -r requirements.txt
```
6. Execute as migrações
```sh
python manage.py makemigrations
python manage.py migrate
```
7. Inicie o servidor
```sh
python manage.py runserver
```
Pronto, agora o sistema está rodando em `localhost:8000`

