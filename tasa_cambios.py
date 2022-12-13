import requests

r = requests.get('https://rest.coinapi.io/v1/exchangerate/ETH/EUR?apikey=15C09B77-2FB4-42B3-ADE4-2C5A31AF426F')

print(r.status_code)
print(r.text)