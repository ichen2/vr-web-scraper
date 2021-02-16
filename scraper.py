import requests
from bs4 import BeautifulSoup

main_url = 'http://historyview.org/'
main_page = requests.get(main_url)

main_soup = BeautifulSoup(main_page.content, 'html.parser')

a_tags = main_soup.find_all(class_='image-wrap')
page_urls = map(lambda url: url['href'], a_tags)

tour_urls = []

#for url in list(page_urls):
tour_page = requests.get(list(page_urls)[0])
tour_soup = BeautifulSoup(tour_page.content, 'html.parser')
print(tour_soup.prettify())
tour_url = tour_soup.find(id='mp-iframe')['src']
tour_urls.append(tour_url)

print(tour_urls)
