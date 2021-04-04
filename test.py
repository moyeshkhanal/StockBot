import requests

apiKey = "WA6ETHZS9B54GOVSZ9GDKLAFHNLNUY7I"
# The QUOTES endpoint
ticker = "TSLA"
endPoint = f"https://api.tdameritrade.com/v1/marketdata/quotes"

payload = {'apikey': apiKey,
'symbol':"MSFT,PLTR"}
# Make request
content = requests.get(url = endPoint, params = payload)


data = content.json()
totalVol = data["MSFT"]["totalVolume"]
print(f'Total Volume is: {totalVol:,}')