from bs4 import BeautifulSoup
import requests
import csv

def fetch_page(url):
	response = requests.get(url)
	if response.status_code != 200: #Error Handling
		print(f"Failed to fetch {url}" "(status code: {response.status_code})")
		return None
	return BeautifulSoup(response.text, "html.parser")
def scrape_quotes(soup):
	quotes = soup.findAll("span", attrs = {"class": "text"})
	authors = soup.findAll("small", attrs = {"class": "author"})
	return zip(quotes, authors)

def get_next_page(soup):
	next_button = soup.find("li", class_="next")
	if next_button:
		next_link = next_button.find("a").get("href")
		return next_link
	else:
		return None

    
base_url = "http://quotes.toscrape.com"
url = base_url
file = "scraped.csv"

with open("scraped.csv", "w", newline="", encoding="utf-8") as file:
	writer = csv.writer(file)
	writer.writerow(["QUOTES", "AUTHORS"]) #Writing Header Row

	while url: #loop for multiple pages
		soup = fetch_page(url)
		if not soup: #break incase page is invalid
			break
		
		#scraping Quotes and Authors
		for quote, author in scrape_quotes(soup):
			print(quote.text + " - " + author.text)
			writer.writerow([quote.text, author.text])
		
		#update to next page url
		next_page = get_next_page(soup)
		if next_page: #if there is another page, append the base url to the new page link
			url = base_url + next_page
		else: #exiting loop if no more pages exist
			url = None
    
