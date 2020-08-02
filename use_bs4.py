import requests
from bs4 import BeautifulSoup

requests.get('https://detik.com')

url = 'https://detik.com'
try:
    response = requests.get(url)
    print(f'success {response}')
    #print(f'Content {response.text}')
    soup = BeautifulSoup (response.text, features="html.parser")
    print(f'Hasil pemmanggilan {url}')
    print(f'Title: {soup.title.string}')
except Exception as e:
    print('There is an error' , e)
print('Program ended')
