
import requests, json, time
from requests.exceptions import HTTPError
from playsound import playsound

def getCoin(coin):
    try:
        url = 'https://api.nomics.com/v1/currencies/ticker?key=a73a76e8378cb82f566695cc70ffa8bc&ids=' + coin + '&interval=1h&convert=USD'
        response = requests.get(url)
        jsonResponse = json.loads(response.text)
        price = jsonResponse[0]["price"]

    except HTTPError as http_err:
        print(f'HTTP error occurred: {http_err}')
    except Exception as err:
        print(f'Other error occurred: {err}')

    return price


def main():
    while(True):
        price = (float) (getCoin('LINK'))
        print(price)
        if(price > 8.6 or price < 8.4):
            playsound('napalm-death.wav')
        time.sleep(60)
        

main()