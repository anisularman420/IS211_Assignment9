import requests
from bs4 import BeautifulSoup

# Define the URL for CBS NFL Stats - Touchdowns
url = "https://www.cbssports.com/nfl/stats/player/passing/nfl/regular/all/?sortcol=td&sortdir=descending"

# Send an HTTP GET request to the URL
response = requests.get(url)

# Check if the request was successful
if response.status_code == 200:
    # Parse the HTML content of the page
    soup = BeautifulSoup(response.text, 'html.parser')

    # Find the table with the touchdown data
    touchdown_table = soup.find("table", {"class": "Tablebase-table"})

    if touchdown_table:
        # Extract and print the top 20 players with their positions, teams, and touchdowns
        for row in touchdown_table.find_all("tr")[1:21]:  # Skip the header row
            columns = row.find_all("td")
            player = columns[0].text.strip()
            position = columns[2].text.strip()
            team = columns[3].text.strip()
            touchdowns = columns[4].text.strip()
            print(f"Player: {player}, Position: {position}, Team: {team}, Touchdowns: {touchdowns}")
    else:
        print("Touchdown table not found on the page.")
else:
    print("Failed to retrieve data from the website.")
