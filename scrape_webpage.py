import requests
from bs4 import BeautifulSoup

def scrape_webpage(url, output_file):
    """
    Scrapes the HTML content of a webpage and saves it to a file.
    
    Args:
    url (str): The URL of the webpage to scrape.
    output_file (str): The file path to save the HTML content.
    """
    try:
        # Send a GET request to the webpage
        response = requests.get(url)
        response.raise_for_status()  # Check for HTTP request errors

        # Parse the HTML content
        soup = BeautifulSoup(response.content, 'html.parser')

        # Get the prettified HTML content
        html_content = soup.prettify()

        # Save the HTML content to a file
        with open(output_file, 'w', encoding='utf-8') as file:
            file.write(html_content)

        print(f'The HTML content has been saved to {output_file}')
    except requests.exceptions.RequestException as e:
        print(f'Failed to retrieve the webpage: {e}')

if __name__ == '__main__':
    # Define the URL of the webpage to scrape
    url = 'https://en.wikipedia.org/wiki/List_of_best-selling_books'
    # Define the output HTML file path
    output_file = 'webpage.html'
    # Scrape the webpage
    scrape_webpage(url, output_file)
