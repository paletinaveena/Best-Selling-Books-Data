import pandas as pd
from bs4 import BeautifulSoup

def html_to_csv(input_file):
    """
    Converts tables from an HTML file to CSV files.
    
    Args:
    input_file (str): The path to the input HTML file.
    """
    try:
        # Read the HTML file content
        with open(input_file, 'r', encoding='utf-8') as file:
            html_content = file.read()

        # Parse the HTML content
        soup = BeautifulSoup(html_content, 'html.parser')

        # Find all tables in the HTML
        tables = soup.find_all('table')

        # Iterate through each table and convert to CSV
        for index, table in enumerate(tables):
            # Use pandas to read the HTML table into a DataFrame
            df = pd.read_html(str(table))[0]

            # Define the output CSV file path
            output_file = f'table_{index+1}.csv'

            # Save the DataFrame to a CSV file
            df.to_csv(output_file, index=False)

            print(f'Table {index+1} has been saved to {output_file}')
    except Exception as e:
        print(f'Failed to convert HTML to CSV: {e}')

if __name__ == '__main__':
    # Define the input HTML file path
    input_file = 'webpage.html'
    # Convert HTML tables to CSV
    html_to_csv(input_file)
