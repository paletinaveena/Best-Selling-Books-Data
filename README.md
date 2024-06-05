# Best-Selling-Books-Data

## Web Scraping and HTML Table to CSV Conversion

This repository contains two Python scripts designed to work together:

1. `scrape_webpage.py`: This script scrapes a specified webpage and saves its HTML content to a file.
2. `html_to_csv.py`: This script reads an HTML file, extracts tables from it, and saves each table as a CSV file.

### Prerequisites

Ensure you have Python 3.x installed on your system. Additionally, install the required libraries using pip:
```bash
pip install requests beautifulsoup4 pandas
```

### Usage
#### Step 1: Scrape a Webpage
The scrape_webpage.py script fetches the HTML content of a specified webpage and saves it to an webpage.html file.

To run the script:

```bash
python scrape_webpage.py
```


#### Step 2: Convert HTML Tables to CSV
The html_to_csv.py script reads the webpage.html file, extracts all tables, and saves each table as a separate CSV file.

To run the script:

```bash
python html_to_csv.py
```


### Example Workflow
Scrape the webpage containing the list of best-selling books from Wikipedia:
```bash
python scrape_webpage.py
```

Convert the extracted tables to CSV files:
```bash
python html_to_csv.py
```

The CSV files will be saved as table_1.csv, table_2.csv, etc., in the same directory.


### Detailed Explanation
`scrape_webpage.py`

This script sends an HTTP GET request to the specified URL, parses the HTML content using BeautifulSoup, and writes the prettified HTML to a file.

`html_to_csv.py`

This script reads the saved HTML file, parses it to find all tables, converts each table into a pandas DataFrame, and writes each DataFrame to a CSV file.

