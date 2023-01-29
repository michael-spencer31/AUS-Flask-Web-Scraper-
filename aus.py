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

print(table)

# print(results.prettify())

