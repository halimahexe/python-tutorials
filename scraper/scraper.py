import requests
from bs4 import BeautifulSoup


def scrape_npm():
    """Scrape @ldn-viz NPM packages for latest svelte 5 versions"""
    url = 'https://www.npmjs.com/package/@ldn-viz/charts?activeTab=versions'
    response = requests.get(url, timeout=100)
    soup = BeautifulSoup(response.text, 'html.parser')
    print(soup.prettify())

# def scrape():
#     """Scrape"""
#     url = 'https://realpython.github.io/fake-jobs/'
#     response = requests.get(url, timeout=100)
#     soup = BeautifulSoup(response.text, 'html.parser')
#     print(soup.prettify())

    # title = soup.select_one('h1').text
    # text = soup.select_one('p').text
    # link = soup.select_one('a').get('href')

    # print(title)
    # print(text)
    # print(link)


if __name__ == '__main__':
    scrape_npm()
