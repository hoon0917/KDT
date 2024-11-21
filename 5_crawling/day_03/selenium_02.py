from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

driver.get('http://www.pythonscraping.com/pages/warandpeace.html')
driver.implicitly_wait(5)

# 하나의 클래스 이름 검색
name = driver.find_element(By.CLASS_NAME, 'green')
print(name)

print('-'*40)

# 해당 클래스 이름을 모두 검색
name_list = driver.find_elements(By.CLASS_NAME,'green')
for i in name_list:
    print(i.text)