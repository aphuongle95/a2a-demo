import requests
import json
import os
from dotenv import load_dotenv

load_dotenv()

api_key = os.environ["OPENWEATHERMAP_API_KEY"]
url = 'http://api.openweathermap.org/data/2.5/weather?q=london&appid=' + api_key
response = requests.get(url)

if response.status_code == 200:
    print('Wohoo! Setup complete!\n\nWe are good to go!')
elif response.status_code == 429:
    print('Your account is temporary blocked due to exceeding of requests limitation of your subscription type. Please choose the proper subscription http://openweathermap.org/price')
else:
    print(f'{response.status_code}: {response.reason}')