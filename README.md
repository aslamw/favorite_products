# Favorite Products

OBS.: Para Rodar o projeto precisa ter docker e docker-compose instalado

## Para inicializar projeto rode os comandos:

```
    docker-compose build

    docker-compose up
```
---
## Se quiser ver o banco de dados é só entrar na rota:
```http
    http://localhost:8080/
```

### Digite:
![Captura de tela de 2023-06-08 16-44-09](https://github.com/aslamw/calculate_world_flask/assets/50378596/2f5c69ed-da48-45aa-bfbd-5c255751dd56)

### Vai abrir uma janela assim:
![Captura de tela de 2023-06-08 16-45-32](https://github.com/aslamw/calculate_world_flask/assets/50378596/4c0f3209-a44b-4935-946d-a0357bff6056)

---

# Configurando o insomnia

### Crie uma pasta e coloque as rotas nela
![Captura de tela de 2023-06-08 14-54-28](https://github.com/aslamw/calculate_world_flask/assets/50378596/2c8a990a-c1ac-47ff-ab29-e7e6505a6df7)

### Configure o Environment

![Captura de tela de 2023-06-08 14-54-58](https://github.com/aslamw/calculate_world_flask/assets/50378596/cdf7efa2-c5c7-4e3c-b3df-d4f035e893f3)

```Json
{
	"local": "http://localhost:7070",
	"token": "Maior_que_a_tristeza-de-nao-haver_vencido_e-a_vergonha_de-nao_ter-lutado"
}
```

![Captura de tela de 2023-06-08 14-55-36](https://github.com/aslamw/calculate_world_flask/assets/50378596/9326f967-7e70-4360-bc26-59c7e3518cc4)

## Exemplo da rota de registro do client

![Captura de tela de 2023-06-08 14-56-04](https://github.com/aslamw/calculate_world_flask/assets/50378596/cb04db6a-4504-4c40-b45f-df091e600cf4)

# OBS.: Para conseguir usar as rotas tem que usar atenticação pelo Headers

![Captura de tela de 2023-06-08 14-56-13](https://github.com/aslamw/calculate_world_flask/assets/50378596/9bcd15a8-1bf1-4a1f-b73e-302999287837)


### A unica rota que não precisa do AUTH é a de teste para ver se a API está funcionando

```http
http://localhost:7070/
```