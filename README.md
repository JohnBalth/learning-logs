Learning Logs

Aplicação web desenvolvida com Django para organizar e registrar aprendizados por meio de tópicos e anotações.

O projeto permite que cada usuário mantenha seus próprios registros de estudo, criando tópicos, adicionando entradas e pesquisando conteúdos já registrados.

Funcionalidades

Cadastro e autenticação de usuários

Criação de tópicos de estudo

Edição e exclusão de tópicos

Criação de entradas dentro de cada tópico

Edição e exclusão de entradas

Pesquisa por tópicos e conteúdos

Associação dos tópicos ao usuário autenticado

Controle de acesso aos dados de cada usuário

Interface administrativa utilizando Django Admin

Configuração de variáveis de ambiente para dados sensíveis

Tecnologias

Python

Django 6.0.7

SQLite

python-dotenv

HTML

CSS

Estrutura do projeto
learning_log/
├── learnig_log/          # Configurações principais do projeto Django
├── learning_logs/        # Aplicação principal
│   ├── migrations/
│   ├── templates/
│   ├── admin.py
│   ├── forms.py
│   ├── models.py
│   ├── tests.py
│   ├── urls.py
│   └── views.py
├── .gitignore
├── manage.py
├── requirements.txt
└── README.md

Como executar o projeto
1. Clone o repositório
git clone https://github.com/JohnBalth/learning-logs.git
cd learning-logs

2. Crie e ative um ambiente virtual

No Windows:

python -m venv ll_env
ll_env\Scripts\activate

3. Instale as dependências
pip install -r requirements.txt

4. Configure as variáveis de ambiente

Crie um arquivo .env na raiz do projeto.

Exemplo:

DJANGO_SECRET_KEY=sua-chave-secreta
DJANGO_DEBUG=True
DJANGO_ALLOWED_HOSTS=127.0.0.1,localhost


O arquivo .env não deve ser enviado para o GitHub.

5. Execute as migrações
python manage.py migrate

6. Inicie o servidor
python manage.py runserver


Depois, acesse:

http://127.0.0.1:8000/

Segurança

O projeto utiliza algumas práticas básicas de segurança:

SECRET_KEY configurada por variável de ambiente

DEBUG configurável por variável de ambiente

ALLOWED_HOSTS configurável por variável de ambiente

Arquivos .env ignorados pelo Git

Banco de dados local ignorado pelo Git

Autenticação obrigatória para áreas privadas

Filtragem dos objetos pelo usuário autenticado

Um ponto importante da aplicação é o controle de acesso aos dados.

Por exemplo, os tópicos são consultados considerando também o usuário autenticado, evitando que um usuário acesse diretamente registros pertencentes a outra conta.

Próximos passos

Algumas melhorias planejadas para versões futuras:

Adicionar testes automatizados

Melhorar a interface e a responsividade

Otimizar consultas ao banco de dados

Melhorar a configuração de produção

Personalizar o Django Admin

Realizar deploy da aplicação

Objetivo do projeto

O Learning Logs foi desenvolvido como projeto de aprendizado e portfólio com o objetivo de praticar conceitos fundamentais do desenvolvimento web utilizando Django, incluindo:

Modelagem de dados

Autenticação

Autorização

CRUD

Formulários

Relacionamentos entre modelos

Consultas ao banco de dados

Organização de aplicações Django

Variáveis de ambiente

Controle de versão com Git e GitHub

Autor

John Balth

GitHub: @JohnBalth