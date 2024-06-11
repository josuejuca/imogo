import requests

key = "CHAVE_API" # CHAVE_API
url = f"https://api.rd.services/platform/conversions?api_key={key}"


payload = {
    "event_type": "CONVERSION",
    "event_family": "CDP",
    "payload": {
        "conversion_identifier": "API DIL", # Tenta deixar assim para eu conseguir identificar o que chegou da Dil 
        "email": "etc@josuejuca.com", # E-mail do LEAD
        "name": "Josué Juca", # Nome do LEAD
        "state": "DF", # Estado 
        "city": "Ceilândia - Ceilândia Sul", # Cidade 
        "country": "Brasil", # Pais 
        "personal_phone": "+55 61 9 8463-4855", # Telefone mask: +55 61 9 0000-0000
        "tags": ["CORRETOR", "prospecção"], # Altere o campo de acordo com o tipo de LEAD usando o ( CORRETOR / LEAD )
    }
}
headers = {
    "accept": "application/json",
    "Content-Type": "application/json"
}

response = requests.post(url, json=payload, headers=headers)

print(response.text)
