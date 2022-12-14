import requests
from utils import apikey

r = requests.get(f'https://rest.coinapi.io/v1/assets/?apikey={apikey}') 

if r.status_code != 200:
    raise Exception( "Error en consulta de assets : {}".format(r.status_code))

lista_general = r.json()
lista_criptos = []

for item in lista_general:
    if item["type_is_crypto"] == 1:
        lista_criptos.append(item['asset_id'])


print("moneda digital:",len(lista_criptos))
print("moneda digital:",len(lista_general) -len(lista_criptos))
moneda_cripto = input('Ingrese una criptomoneda conocida: ').upper()

while moneda_cripto != "" and moneda_cripto.isalpha():

    if moneda_cripto in lista_criptos:
        r = requests.get(f'https://rest.coinapi.io/v1/exchangerate/{moneda_cripto}/EUR?apikey={apikey}')    

        print(r.status_code)
        print(r.text)

        resultado = r.json()


        if r.status_code == 200:
            print("{:,.2f}€".format(resultado['rate']))#.replace(',','.')
        else:
            print(resultado['error'])
    moneda_cripto = input('Ingrese una criptomoneda conocida: ').upper()
