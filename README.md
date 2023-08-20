# API Super Mario Bros.

API para fornecer informações sobre os principais jogos de plataforma da franquia Super Mario Bros, com imagens, vendas, data de lançamento, imagens de gameplay e mais, incluindo também dois filtros (console e ano). Criei essa API para fins de estudos, portanto trata-se de um projeto simples, com poucos end-points e único método (GET). 

Espero que goste e lhe sirva para seus projetos Nintendistas 😁

## Endpoints Disponíveis

### Listar Jogos

**Endpoint:** `/api/jogos`

Retorna a lista de jogos da franquia Super Mario.

Parâmetros de Query:

- `console` (opcional): Filtra os jogos por console.
- `ano` (opcional): Filtra os jogos por ano de lançamento.

Exemplo de Uso:

![image](https://github.com/oliveiratales/api-mario-bros/assets/118945743/f8646030-c634-4923-9e89-1682d1f34517)
![image](https://github.com/oliveiratales/api-mario-bros/assets/118945743/5706f2d3-4d4c-464b-89fd-cfddd7ea3bdc)

### Detalhes do Jogo

**Endpoint:** `/api/jogos/{id}`

Retorna os detalhes de um jogo específico pelo seu ID.

Parâmetros de Path:

- `id`: ID do jogo.

Exemplo de Uso:

![image](https://github.com/oliveiratales/api-mario-bros/assets/118945743/6ddd4183-659f-4c58-ad0d-2fe519ecc49d)

## Campos de Resposta

- `id`: ID do jogo.
- `nome`: Nome do jogo.
- `data_lancamento`: Data de lançamento do jogo.
- `console`: Console em que o jogo foi lançado.
- `vendas`: Número de vendas do jogo.
- `capa`: URL da capa do jogo.
- `avaliacao`: Avaliação do jogo.
- `sinopse`: Sinopse do jogo.
- `gameplay1`: URL de uma imagem de gameplay.
- `gameplay2`: URL de uma imagem de gameplay.
- `gameplay3`: URL de uma imagem de gameplay.

## Exemplos de Respostas

### Listar Jogos

```json
[
  {
    "id": 1,
    "nome": "Super Mario Bros.",
    "data_lancamento": "1985-09-13",
    "console": "NES",
    "vendas": 40.24,
    "capa": "link_para_capa",
    "avaliacao": 9.2,
    "sinopse": "Descrição do jogo...",
    "gameplay1": "link_para_gameplay_1",
    "gameplay2": "link_para_gameplay_2",
    "gameplay3": "link_para_gameplay_3"
  },
  // Outros jogos...
]

```

### Detalhes do Jogo

```json
{
  "id": 1,
  "nome": "Super Mario Bros.",
  "data_lancamento": "1985-09-13",
  "console": "NES",
  "vendas": 40.24,
  "capa": "link_para_capa",
  "avaliacao": 9.2,
  "sinopse": "Descrição do jogo...",
  "gameplay1": "link_para_gameplay_1",
  "gameplay2": "link_para_gameplay_2",
  "gameplay3": "link_para_gameplay_3"
}

```
