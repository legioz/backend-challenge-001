### Documentação

[Documentação da API via OpenAPI3/Swagger](http://localhost/api/docs)


##### Estrutura do .env no diretório /src 

```sh
DEBUG=True
PROJECT_NAME=API Luiz
SECRET_KEY=l1d2b99ae9f502cd9bbb3c345

MARIADB_USER=user
MARIADB_PASS=123456
MARIADB_HOST=db
MARIADB_DB=db

```


##### Build e execução dos containeres
```sh
docker-compose up --build -d
```

##### Finalizar execução dos containeres
```sh
docker-compose down
```

O deploy da aplicação pode ser executado utilizando o docker-compose para orquestrar os containers da api do backend
fazendo a integração com alguma pipeline para CI/CD do servidor.
Durante o ambiente de produção é interessante trocar as váriaveis de conexão ao banco de dados e alterar DB-default no settings.py 
para implementar o novo banco de dados mais robusto descontainerizado invés do sqlite que foi usado apenas para desenvolvimento.
