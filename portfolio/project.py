from bs4 import BeautifulSoup
import requests


def scrape():
    url = 'https://fac-standard.netlify.app/project/criteria/'
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    # print(soup)

    main = soup.select_one('main')
    line_items = main.find_all('li')

    for li in line_items:
        descs = li.find_all('p', attrs={"class": None}, limit=2)
        desc = ''
        for d in descs:
            desc += d.text + '\n'

        ksbs = li.select('a.Pill')
        ksb = ''
        for k in ksbs:
            ksb += f"{k.text}, "

        print()
        print(f"{ksb}: {desc}")


if __name__ == '__main__':
    scrape()
