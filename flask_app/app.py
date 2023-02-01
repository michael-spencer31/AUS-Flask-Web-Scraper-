from flask import Flask, render_template
import requests
import pandas as pd

app = Flask(__name__)

@app.route('/')
def home():

	headers = {
	    'Connection': 'keep-alive',
	    'Cache-Control': 'max-age=0',
	    'Upgrade-Insecure-Requests': '1',
	    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.102 Safari/537.36',
	    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
	    'Sec-Fetch-Site': 'cross-site',
	    'Sec-Fetch-Mode': 'navigate',
	    'Sec-Fetch-User': '?1',
	    'Sec-Fetch-Dest': 'document',
	    'Referer': 'https://www.jpx.co.jp/english/markets/index.html',
	    'Accept-Language': 'de-DE,de;q=0.9,en-US;q=0.8,en;q=0.7,it;q=0.6,la;q=0.5',
	}

	womens_response = requests.get('https://www.atlanticuniversitysport.com/sports/wice/2022-23/standings', headers=headers)
	mens_response = requests.get('https://www.atlanticuniversitysport.com/sports/mice/2022-23/standings', headers=headers)

	womens_table = pd.read_html(womens_response.text, attrs={"class": "stats-table"})[0]
	mens_table = pd.read_html(mens_response.text, attrs={"class": "stats-table"})[0]

	return render_template("home.html", womens_standings=[womens_table.to_html(classes='data')], titles=womens_table.columns.values, mens_standings=[mens_table.to_html(classes='data')], mens_titles=mens_table.columns.values)

@app.route("/POST")
def standings():
	return "Hello, World!"


if __name__ == "__main__":
	app.run(debug=True)