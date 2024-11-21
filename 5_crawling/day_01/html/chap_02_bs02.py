from bs4 import BeautifulSoup
soup = BeautifulSoup(html_example, 'htmal.parser')

print(soup.title)

print(soup.h1)