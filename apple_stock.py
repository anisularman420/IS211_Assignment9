import requests
from bs4 import BeautifulSoup

# Define the URL for Apple's stock historical prices on Yahoo Finance
url = "https://finance.yahoo.com/quote/AAPL/history?p=AAPL&guccounter=1"

# Send an HTTP GET request to the URL
response = requests.get(url)

# Check if the request was successful
if response.status_code == 200:
    # Parse the HTML content of the page
    soup = BeautifulSoup(response.text, 'html.parser')

    # Find the historical prices table
    price_table = soup.find("table", {"data-test": "historical-prices"})

    if price_table:
        # Extract and print the close price and date for all the dates shown on the page
        for row in price_table.find_all("tr")[1:]:
            columns = row.find_all("td")
            date = columns[0].text.strip()
            close_price = columns[4].text.strip()
            print(f"Date: {date}, Close Price: {close_price}")
    else:
        print("Historical prices table not found on the page.")
else:
    print("Failed to retrieve data from the website.")
