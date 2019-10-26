# Criando a pasta do projeto web django (cmd)
# connectedin é o nome do projeto
django-admin.py startproject connectedin

# Criando as tabelas do SQLite (vem com o Django)
python manage.py migrate

# Subir o servidor web
python manage.py runserver

# Criando um App dentro do nosso projeto
python manage.py startapp perfis

# Criar a pasta templates dentro do app para armazenar as paginas html do site

# Fazer uma migration para propagar as mudanças feitas no modelo para o banco de dados
python manage.py makemigrations

# Replicar o modelo do migrations para o banco de dados
python manage.py migrate

# Abrir o Shell do Django
python manage.py shell

# Salvando um registro no banco atrás de Save() que foi herdada da classe Models
perfil = Perfil(nome='Rogerio', email='rogeriosouzax@hotmail.com', telefone='199999', nome_empresa='E-Corp')
perfil.save()

# Retornar registros do banco
perfil_encontrado = Perfil.objects.get(id=1)