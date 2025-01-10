from bs4 import BeautifulSoup
import requests
import csv

def fetch_page(url):
	response = requests.get(url)
    if response.status_code != 200: #Error Handling
    	print(f"Failed to fetch {url}" (status code: {response.status_code})")
    	return None
    return BeautifulSoup(response.text, "html.parser")
def scrape_quotes(soup):
	quotes = soup.findAll("span", attrs = {"class": "text"})
	authors = soup.findAll("small", attrs = {"class": "author"})
	return zip(quotes, authors)
    
url = "http://quotes.toscrape.com"
soup = fetch_page(url)

if soup:
	with open("scraped.csv", "w", newline="") as file:
    	writer = csv.writer(file)
    	writer.writerow(["QUOTES", "AUTHORS"])
		for quote, author in scrape_quotes(soup):
    		print(quote.text + " - " + author.text)
    		writer.writerow([quote.text, author.text])
else:
    print("Nothing worth scraping here.")