# API Super Mario Bros.

Esta documentação descreve os endpoints e as funcionalidades da API Super Mario, que fornece informações sobre os principais jogos de plataforma da franquia Super Mario Bros.

## Endpoints Disponíveis

### Listar Jogos

**Endpoint:** `/api/jogos`

Retorna a lista de jogos da franquia Super Mario.

Parâmetros de Query:

- `console` (opcional): Filtra os jogos por console.
- `ano` (opcional): Filtra os jogos por ano de lançamento.

Exemplo de Uso:



### Detalhes do Jogo

**Endpoint:** `/api/jogos/{id}`

Retorna os detalhes de um jogo específico pelo seu ID.

Parâmetros de Path:

- `id`: ID do jogo.

Exemplo de Uso:



## Campos de Resposta

- `id`: ID do jogo.
- `nome`: Nome do jogo.
- `data_lancamento`: Data de lançamento do jogo.
- `console`: Console em que o jogo foi lançado.
- `vendas`: Número de vendas do jogo.
- `capa`: URL da capa do jogo.
- `avaliacao`: Avaliação do jogo.
- `sinopse`: Sinopse do jogo.
- `gameplay1`: URL do vídeo de gameplay 1.
- `gameplay2`: URL do vídeo de gameplay 2.
- `gameplay3`: URL do vídeo de gameplay 3.

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

### Detalhes do Jogo

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