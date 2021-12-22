# Formação Django 

Curso: https://cursos.alura.com.br/formacao-django  
Documentação oficial: https://docs.djangoproject.com/pt-br/2.2/  

## Módulo 1 - Iniciando com Django

### Curso de Introdução ao Django: Modelo, Rotas e Views

- Aprenda a desenvolver aplicações web utilizando a linguagem Python
- Desenvolva uma aplicação do zero, seguindo as principais convenções e boas práticas
- Saiba como configurar e conectar sua aplicação com um banco de dados sql
- Melhore seu código, reaproveitando em outras partes da aplicação
- Entenda a arquitetura de uma aplicação feita com Django
 

01. Iniciando aplicação e subindo o servidor
- Criamos uma pasta para manter todo código da nossa aplicação;
- Utilizamos o módulo venv, que fornece suporte para a criação de ambientes virtuais leves com seus próprios diretórios, opcionalmente isolados dos diretórios do sistema;
- Utilizamos o pip para instalar o Django em nosso ambiente virtual;
- Iniciamos o desenvolvimento da nossa aplicação com o comando django-admin start project alurareceita e subimos o servidor com o comando python manage.py runserver.

2. Template, rotas e views
- Criamos uma pasta templates dentro do app de receitas, para manter nossos arquivos html;
- Importamos uma página estilizada, com html, css e javascript;
- Carregamos esses arquivos, conhecidos como arquivos estáticos e melhoramos o visual da nossa aplicação.

03. Links, extends e partials
- Ajustamos os links da index, do logo através da template tag url;
- Criamos o base.html para usar as mesmas partes do HTML em diferentes páginas da aplicação;
- Evitamos código duplicado do menu e do footer criando e incluindo partials.

04. Modelo e banco de dados
- Aprendemos como enviar dados para o template renderizar;
- Instalamos e configuramos o banco de dados Postgres com a nossa aplicação;
- Criamos o modelo de receitas e mapeamos para uma tabela no banco de dados.
- Utilizamos {% %}, para processamento sem exibir na tela, como {% load static %} por exemplo.
- Utilizamos {{ }}, para renderizar variáveis no template por exemplo.

05. Admin, parâmetros e receitas
- Aprendemos como enviar e exibir dados para uma página;
- Exibimos as receitas que estão no banco de dados;
- Alteramos a url da index, exibindo como cada receita é feita, seus ingredientes e outras informações.

