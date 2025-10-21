import requests

API_CEP = "https://cep.awesomeapi.com.br/json/"
GOOGLE = "https://www.google.com/search"


def buscar_cep(cep_usuario):
    url_api = f"{API_CEP}/{cep_usuario}"

    resposta = requests.get(cep_usuario)

    if resposta.status_code == 200:
        dados = resposta.json()
        return dados

    else:
        return None
    

def descobrir_cep(endereco_usuario):
    resposta = requests.get(GOOGLE, params={"q": endereco_usuario})
    return resposta.url



