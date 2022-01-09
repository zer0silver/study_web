import requests
from bs4 import BeautifulSoup

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}
data = requests.get('https://movie.naver.com/movie/sdb/rank/rmovie.nhn?sel=pnt&date=20200303', headers=headers)

soup = BeautifulSoup(data.text, 'html.parser')

# title = soup.select_one('#old_content > table > tbody > tr:nth-child(2) > td.title > div > a')
# print(title.text)  # 태그의 텍스트 가져오기 , 그린북
# print(title['href'])  # 태그의 속성 가져오기

# ---------------------------------------------------------------------
# <사용 코드 참고>
# old_content > table > tbody > tr:nth-child(2)
# old_content > table > tbody > tr:nth-child(2) > td:nth-child(1) > img
# old_content > table > tbody > tr:nth-child(2) > td.point

trs = soup.select('#old_content > table > tbody > tr')

for tr in trs:
    a_tag = tr.select_one('td.title>div>a')
    a_point = tr.select_one('td.point')
    a_rank = tr.select_one('td:nth-child(1) > img')
    if a_tag is not None:
        title = a_tag.text
        point = a_point.text
        rank = a_rank['alt']
        print(rank,title,point)
