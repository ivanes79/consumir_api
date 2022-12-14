import requests
from config import apikey

moneda_cripto = input('Ingrese una criptomoneda conocida: ').upper()

while moneda_cripto != "" and moneda_cripto.isalpha():

    if moneda_cripto in lista_criptos:
        r = requests.get(f'https://rest.coinapi.io/v1/exchangerate/{moneda_cripto}/EUR?apikey={apikey}')    



        print(r.status_code) #CODIGO 200 CORRECTO
        print(r.text)

        resultado = r.json()#GUARDAMOS EL R.JSON EN RESULTADO QUE ES UN DICCIONARIO EN PYTHON


        if r.status_code == 200:
            #valor =  round(resultado['rate'],4)
            #print(f"{valor} €")
            print("{:,.2f}€".format(resultado['rate']))#.replace(',','.')
        else:
            print(resultado['error'])
        moneda_cripto = input('Ingrese una criptomoneda conocida: ').upper()
