import requests
from bs4 import BeautifulSoup


def scrape():
    url = 'https://fac-standard.netlify.app/portfolio/criteria/'
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    # print(soup)

    main = soup.select_one('main')
    line_items = main.find_all('li')

    for li in line_items:
        desc = li.find('p').text
        ksb = li.select_one('a.Pill').text
        print()
        print(f"{ksb}: {desc}")


if __name__ == '__main__':
    scrape()
