from bs4 import BeautifulSoup
soup = BeautifulSoup(open('soup_text.html',encoding='utf8'),'lxml')
print(soup.select('.tang > ul > li > a')[0]['href'])