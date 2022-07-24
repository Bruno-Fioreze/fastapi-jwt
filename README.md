### Descrição da aplicação
API Dockerizada feita em FastAPI.

### Dependências

- Docker
- Docker Compose

### Como executar

```bash
    #entre na raiz do projeto e rode esse comando
    sudo chmod 777 ./entrypoint.sh
    
    #builda e sobe
    sudo docker-compose up -d --build

    #veja os logs
    sudo docker-compose logs 

    #tente acessar a aplicação pelo endereço: http://localhost:8000/
```
