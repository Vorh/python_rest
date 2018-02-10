import requests
from bs4 import BeautifulSoup


def download(url, file_name):
    with open('/home/vorh/Media/Music/Plamenev/' +file_name, 'wb') as file:
        response = requests.get(url)
        file.write(response.content)


URL = 'http://plamenev.ru'

with open('site.html', 'r') as myfile:
    data = myfile.read()

soap = BeautifulSoup(data, 'html.parser')

list = soap.find('ul', {"id": "playlist1"})

listLi = list.find_all('li')

for li in listLi:
    link = li.attrs['data-mp3']
    name = link.replace('/audio/', '')
    link = URL + link
    print('Link: %s, name: %s' % (link, name))
    download(link, name)
