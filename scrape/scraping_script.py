from bs4 import BeautifulSoup
import pandas as pd
import requests
from config import BUCKET_NAME, BRONZE_LAYER_PATH, MINIO_ACCESS_KEY, MINIO_SECRET_KEY, ENDPOINT

def scrape_and_save():
    # Send a GET request to the URL
    url = 'https://www.espn.com/soccer/schedule'
    response = requests.get(url)

    # Create a BeautifulSoup object
    soup = BeautifulSoup(response.content, 'html.parser')

    # Find all the table rows containing the football schedule
    table_rows = soup.select('tbody tr')

    # Create a list of dictionaries to store the extracted data
    data = []

    # Iterate over the rows and extract the team names and dates
    for row in table_rows:
        columns = row.select("td")
        if len(columns) >= 3:
            team1 = columns[0].text.strip()
            team2 = columns[1].text.strip()
            time = columns[2].text.strip()
            location = columns[4].text.strip()
            data.append({'home_team': team1, 'away_team': team2, 'time': time, 'location': location})

    # Create a pandas DataFrame from the extracted data
    df = pd.DataFrame(data)

    # Save the DataFrame to a CSV file
    csv_filename = 'football_schedule.csv'
    df.to_csv(csv_filename, index=False)

    # Upload the CSV file to MinIO
    from minio import Minio
    minio_client = Minio(ENDPOINT, access_key=MINIO_ACCESS_KEY, secret_key=MINIO_SECRET_KEY)
    minio_client.fput_object(BUCKET_NAME, f'{BRONZE_LAYER_PATH}/{csv_filename}', csv_filename)

    print('Done.')