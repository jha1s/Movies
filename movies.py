import requests
from bs4 import BeautifulSoup

URL = 'https://movie.naver.com/movie/running/current.nhn'

response = requests.get(URL)
soup = BeautifulSoup(response.text, 'html.parser')

movies_section = soup.select('#content > div.article > div:nth-child(1) > div.lst_wrap > ul > li')

movie_list = []

for movie in movies_section:
    title = movie.select_one('dl > dt > a')
    movie_info = {
        'title' : title.text,'code' : title['href'].split('=')[1]
    }
    movie_list.append(movie_info)

print(movie_list)