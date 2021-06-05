import requests
from bs4 import BeautifulSoup
from time import sleep
for i in range(1,9):
    url = f'https://alta.ge/smartphones-page-{i}.html'
    r = requests.get(url)
    print(r)
    content = r.text

    soup = BeautifulSoup(content, 'html.parser')
    div = soup.find('div', {'class': 'grid-list'})
    f = open('file.csv', 'a')
    for x in div.find_all('div'):
        try:
            name = x.find('a', {'class': 'product-title'})
            print(name.text)

            f.write(name.text + '\n')
        except:
            pass
    sleep(15)



