import requests

data = requests.get('https://api.coindesk.com/v1/bpi/currentprice/USD.json').json()
bpi = data['bpi']
USD = bpi['USD']
rate = USD['rate']
print(f'rate is {rate}')