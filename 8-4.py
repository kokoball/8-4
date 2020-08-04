import requests
from bs4 import BeautifulSoup

URL = "https://movie.naver.com/movie/running/current.nhn"
response = requests.get(URL)

soup = BeautifulSoup(response.text, "html.parser")

movie_data = []
news_section = soup.select(
    'div[id=wrap] > div[id=container] > div[id=content] > div.article > div.obj_section > div.lst_wrap > ul.lst_detail_t1 > li')


for news in news_section:
    a_tag = news.select_one('dl > dt > a')
    movie_title = a_tag.text
    #movie_title = str(a_tag)[44:-4]
    movie_code = a_tag['href'][28:]

    print(movie_title)
    print(movie_code, '\n')
