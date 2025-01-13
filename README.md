# Quotes Web Scraper

This project is a simple web scraper built in Python that extracts quotes and their authors from the website [Quotes to Scrape](http://quotes.toscrape.com) and saves the data into a CSV file (`scraped.csv`). The scraper uses the `BeautifulSoup` library to parse the HTML and the `requests` library to fetch web pages. This project serves as a demonstration of web scraping, ethical coding practices, and efficient use of Python libraries.

---

## Features

- **Dynamic Web Scraping**: Extracts quotes and their respective authors from the website.
- **Pagination Support**: Automatically navigates through all pages of the website to scrape all available quotes.
- **CSV Export**: Saves the scraped data into a CSV file (`scraped.csv`) for easy access and future use.
- **Error Handling**: Handles HTTP errors gracefully by checking response status codes before proceeding.
- **UTF-8 Encoding**: Ensures proper handling of special characters in the scraped quotes and authors.
- **Reusable Functions**:
  - `fetch_page(url)`: Fetches and parses the webpage content using BeautifulSoup.
  - `scrape_quotes(soup)`: Extracts quotes and authors from the parsed HTML.
  - `get_next_page(soup)`: Identifies the "Next" button link for pagination.

---

## Ethical Coding Practices

This project adheres to the following ethical coding practices:

1. **Respect for Websites**:
   - The scraper respects the website’s structure and does not overload the server with unnecessary requests.
   - It is designed to scrape only publicly available data intended for educational or testing purposes.

2. **Avoiding Misuse**:
   - The tool is not intended for unauthorized data collection or scraping websites without permission. Always check a website’s `robots.txt` file before scraping.
   - Data collected using this scraper should not be used for commercial purposes or redistributed without proper credit.

3. **Transparency and Documentation**:
   - The project is well-documented to ensure clarity and responsible use.
   - This `README.md` explicitly states the purpose and ethical guidelines for using the scraper.

4. **Error Handling and Debugging**:
   - The scraper includes error-handling mechanisms to prevent unexpected crashes and provide meaningful feedback to users.

---

## Installation and Usage

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/yourusername/quotes-web-scraper.git
   cd quotes-web-scraper
   ```

2. **Install Required Libraries**:
   Make sure you have Python installed, then install the required libraries:
   ```bash
   pip install requests beautifulsoup4
   ```

3. **Run the Script**:
   ```bash
   python main.py
   ```

   The script will fetch quotes from the website, navigate through all pages, and save them in the `scraped.csv` file.

---

## Example Output

Sample output saved in `scraped.csv`:

| QUOTES                                                                 | AUTHORS         |
|------------------------------------------------------------------------|-----------------|
| "The greatest glory in living lies not in never falling, but in rising every time we fall." | Nelson Mandela  |
| "The way to get started is to quit talking and begin doing."           | Walt Disney     |
| “Your time is limited, so don’t waste it living someone else’s life.” | Steve Jobs      |

---

## Future Improvements

- Expand data extraction to include metadata such as tags or categories associated with each quote.
- Implement multithreading for faster scraping.

---

## License

This project is licensed under the MIT License. Feel free to use and modify the code for personal or educational purposes, but always respect ethical scraping practices.

---

## Disclaimer

This project was created for educational purposes only.

# Quotes Web Scraper

This project is a simple web scraper built in Python that extracts quotes and their authors from the website [Quotes to Scrape](http://quotes.toscrape.com) and saves the data into a CSV file (`scraped.csv`). The scraper uses the `BeautifulSoup` library to parse the HTML and the `requests` library to fetch web pages. This project serves as a demonstration of web scraping, ethical coding practices, and efficient use of Python libraries.

---

## Features

- **Dynamic Web Scraping**: Extracts quotes and their respective authors from the website.
- **Pagination Support**: Automatically navigates through all pages of the website to scrape all available quotes.
- **CSV Export**: Saves the scraped data into a CSV file (`scraped.csv`) for easy access and future use.
- **Error Handling**: Handles HTTP errors gracefully by checking response status codes before proceeding.
- **UTF-8 Encoding**: Ensures proper handling of special characters in the scraped quotes and authors.
- **Reusable Functions**:
  - `fetch_page(url)`: Fetches and parses the webpage content using BeautifulSoup.
  - `scrape_quotes(soup)`: Extracts quotes and authors from the parsed HTML.
  - `get_next_page(soup)`: Identifies the "Next" button link for pagination.

---

## Ethical Coding Practices

This project adheres to the following ethical coding practices:

1. **Respect for Websites**:
   - The scraper respects the website’s structure and does not overload the server with unnecessary requests.
   - It is designed to scrape only publicly available data intended for educational or testing purposes.

2. **Avoiding Misuse**:
   - The tool is not intended for unauthorized data collection or scraping websites without permission. Always check a website’s `robots.txt` file before scraping.
   - Data collected using this scraper should not be used for commercial purposes or redistributed without proper credit.

3. **Transparency and Documentation**:
   - The project is well-documented to ensure clarity and responsible use.
   - This `README.md` explicitly states the purpose and ethical guidelines for using the scraper.

4. **Error Handling and Debugging**:
   - The scraper includes error-handling mechanisms to prevent unexpected crashes and provide meaningful feedback to users.

---

## Installation and Usage

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/yourusername/quotes-web-scraper.git
   cd quotes-web-scraper
   ```

2. **Install Required Libraries**:
   Make sure you have Python installed, then install the required libraries:
   ```bash
   pip install requests beautifulsoup4
   ```

3. **Run the Script**:
   ```bash
   python main.py
   ```

   The script will fetch quotes from the website, navigate through all pages, and save them in the `scraped.csv` file.

---

## Example Output

Sample output saved in `scraped.csv`:

| QUOTES                                                                 | AUTHORS         |
|------------------------------------------------------------------------|-----------------|
| "The greatest glory in living lies not in never falling, but in rising every time we fall." | Nelson Mandela  |
| "The way to get started is to quit talking and begin doing."           | Walt Disney     |
| “Your time is limited, so don’t waste it living someone else’s life.” | Steve Jobs      |

---

## Future Improvements

- Expand data extraction to include metadata such as tags or categories associated with each quote.
- Implement multithreading for faster scraping.

---

## License

This project is licensed under the MIT License. Feel free to use and modify the code for personal or educational purposes, but always respect ethical scraping practices.

---

## Disclaimer

This project was created for educational purposes only.



