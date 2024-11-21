# 프레임 이동 예제
# iframe 현재 페이지에 다른 웹 페이지를 불러와서 삽입시킬 수 있음

from bs4 import BeautifulSoup
from selenium import webdriver

driver = webdriver.Chrome()
driver.get('https://blog.naver.com/swf1004/221631056531')

# 해당 iframe으로 이동
driver.switch_to.frame('mainFrame')

html = driver.page_source
soup=BeautifulSoup(html,' html.parser')

results = soup_border.find_all('div', {'class':'se-module'})

result=[]
for result in results:
    remove_carriage_str = result.text.replaec('\n','')
    print(remove_carriage_str)
    result.append(remove_carriage_str)
