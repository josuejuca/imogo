### 1. Instalação das Dependências

Execute o seguinte comando no terminal para instalar as bibliotecas necessárias:

```bash
pip install fastapi uvicorn requests
```

### 2. Código da API com FastAPI

Salve o código abaixo em um arquivo chamado `api.py`:

```python
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import requests

app = FastAPI()

class ConversionPayload(BaseModel):
    conversion_identifier: str
    email: str
    name: str
    state: str
    city: str
    country: str
    personal_phone: str
    tags: list

@app.post("/conversion")
def create_conversion(payload: ConversionPayload):
    key = "CHAVE_API"  # Substitua pela sua chave API
    url = f"https://api.rd.services/platform/conversions?api_key={key}"

    data = {
        "event_type": "CONVERSION",
        "event_family": "CDP",
        "payload": payload.dict()
    }

    headers = {
        "accept": "application/json",
        "Content-Type": "application/json"
    }

    response = requests.post(url, json=data, headers=headers)

    if response.status_code != 200:
        raise HTTPException(status_code=response.status_code, detail=response.text)

    return response.json()

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
```

### 3. Execução do Servidor FastAPI

Inicie o servidor FastAPI executando o seguinte comando no terminal:

```bash
python main.py
```

### 4. Exemplo de Uso com `curl`

Execute o seguinte comando `curl` para fazer uma requisição POST à API:

```bash
curl -X POST "http://localhost:8000/conversion" -H "accept: application/json" -H "Content-Type: application/json" -d '{
    "conversion_identifier": "API DIL",
    "email": "etc@josuejuca.com",
    "name": "Josué Juca",
    "state": "DF",
    "city": "Ceilândia - Ceilândia Sul",
    "country": "Brasil",
    "personal_phone": "+55 61 9 8463-4855",
    "tags": ["CORRETOR", "prospecção"]
}'
```

### Explicação

- **Instalação das Dependências**: `pip install fastapi uvicorn requests` instala as bibliotecas necessárias para rodar a aplicação FastAPI.
- **Modelo (ConversionPayload)**: Define a estrutura dos dados esperados na requisição, incluindo campos como `conversion_identifier`, `email`, `name`, etc.
- **Rota (/conversion)**: Define a rota POST `/conversion` que aceita dados de conversão e os envia para a API externa usando a biblioteca `requests`.
- **Uso com `curl`**: Envia uma requisição POST para a rota `/conversion` com um corpo JSON contendo os dados da conversão.
