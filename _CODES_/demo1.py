import requests
from bs4 import BeautifulSoup

# Define the URL of the page
url = "https://portswigger.net/web-security/all-topics"

# Send an HTTP request to the website
response = requests.get(url)

# Parse the page content with BeautifulSoup
soup = BeautifulSoup(response.content, 'html.parser')

# Find all <a> tags
a_tags = soup.find_all('a')

# Initialize counter
count = 1

# Loop through all <a> tags to find <h3> inside them and extract href values
for a_tag in a_tags:
    # Look for <h3> inside each <a> tag
    h3_tag = a_tag.find('h3')
    if h3_tag and a_tag.has_attr('href'):
        href_value = a_tag['href']  # Get the href attribute
        a_value = h3_tag.get_text(strip=True)  # Get the text inside <h3>

        # Print the formatted text with numbered prefix and href
        print(f"{count}. [{a_value}]({href_value})")

        # Increment counter and reset to 1 when it reaches 14
        count += 1
        if count == 21:
            count = 1
