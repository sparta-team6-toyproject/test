import requests
from bs4 import BeautifulSoup

headers = {'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}
data = requests.get('https://travel.naver.com/overseas?seasonTab=theme&type=SC&theme=%EC%8B%A0%ED%98%BC&page=1',headers=headers)

soup = BeautifulSoup(data.text, 'html.parser')

names = soup.select('#OverseasHome > div.season_Seasonals__3IGq4 > ul > li')

for name in names:
    a = name.select_one('div > div.item_keywords__ZF5rC > a')

print(a)
#OverseasHome > div.season_Seasonals__3IGq4 > ul > li:nth-child(1) > div > a.item_anchor___k2hT > div.head > span

#OverseasHome > div.season_Seasonals__3IGq4 > ul > li:nth-child(1) > div > div.item_keywords__ZF5rC > a:nth-child(1)