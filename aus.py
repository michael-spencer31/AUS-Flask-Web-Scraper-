from urllib.request import Request, urlopen
from bs4 import BeautifulSoup
import lxml.html as lh
import pandas as pd

req = Request(
	url='https://www.atlanticuniversitysport.com/sports/wice/2022-23/standings',
	headers={'User-Agent': 'Mozilla/5.0'}
)
webpage = urlopen(req).read()

soup = BeautifulSoup(webpage, "html.parser")

results = soup.find(id="mainbody")
table = soup.find('table', class_= "stats-table")

rows = table.find_all("tr")

for row in rows[1:]:
	cells = row.find_all(['td', 'th'])

	cells_text = [cell.get_text(strip=True) for cell in cells]
	print(cells_text)



