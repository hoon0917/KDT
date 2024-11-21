# selenium API 텍스트 입력 예제(네이버 로그인)
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# user agent 정보 추가
agent_option = webdriver.ChromeOptions()
user_agent_string = 'Mozilla/5.0'
agent_option.add_argument('user-agent='+user_agent_string)

driver = webdriver.Chrome(options=agent_option)
driver.get('http://nid.naver.com/nidlogin.login')

# input의 이름이 id 검색
driver.find_element(By.NAME, 'id').send_keys('ancient0917')
driver.find_element(By.NAME, 'pw').send_keys('Ikinye528!')

driver.find_element(By.ID, 'log.login').click()
time.sleep(3)
driver.quit()