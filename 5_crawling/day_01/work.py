from bs4 import BeautifulSoup
from urllib.request import urlopen

page = urlopen('https://forecast.weather.gov/MapClick.php?lat=37.7772&lon=-122.4168')
html = BeautifulSoup(page.read(),'html.parser')
# print(html.read())


# select(), select_all() 함수 사용
def scraping_use_select(html) :
    div_urls = html.select('li.forecast-tombstone')
    for d in div_urls:
        day=d.select_one('p.period-name')
        print(day)
    for c in div_urls:
        cloud=c.select_one('p.short-desc')
        print(cloud)
    for t in div_urls:
        temp=t.select_one('p.temp temp-low')
        print(temp)
    for t2 in div_urls:
        title=t2.select_one('img.forecast-icon')
        print(title)

#link1 = soup.select_one('div#link > a.external_link')
   
# scraping_use_select(html)

# find(), find_all() 함수 사용
def scarping_use_find(html):
    div_urls = html.find_all('li', {'class':'forecast-tombstone'})
    print(len(div_urls), div_urls)
    for d in div_urls:
        day= d.find('p',{'class':'period-name'})
        print(day)
    for c in div_urls:
        cloud= c.find('p',{'class':'short-desc'})
        print(cloud)
    for t in div_urls:
        temp= t.find('p',{'class':'temp temp-low'})
        print(temp)
    for d in div_urls:
        day= d.find('img',{'class':'forecast-icon'})
        print(day)

scarping_use_find(html)