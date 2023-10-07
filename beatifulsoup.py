import requests
from bs4 import BeautifulSoup

url = "https://www.melon.com/chart/index.htm"

header = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8'
}

response = requests.get(url, headers=header)
html = response.text

soup = BeautifulSoup(html, "html.parser")

title = soup.select_one('#lst50 > td:nth-child(6) > div > div > div.ellipsis.rank01 > span > a').text

print(title)


