from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import requests

app = FastAPI()

key = "API_KEY"  # Substitua pela sua chave API

# Modelo para representar os dados da conversão
class ConversionPayload(BaseModel):
    conversion_identifier: str
    email: str
    name: str
    state: str
    city: str
    country: str
    personal_phone: str
    tags: list

# Rota para a conversão
@app.post("/conversion")
def create_conversion(payload: ConversionPayload):
    
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

# Exemplo de uso
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
