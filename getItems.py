import requests
import json
from datetime import datetime, timedelta
import time

# Start and end dates
start_date = datetime(2023, 10, 1)
end_date = datetime(2024, 9, 18)

# URL for the GET request
url = 'https://poit.bolagsverket.se/poit/rest/SokKungorelse'

# Iterate through each day in the range
current_date = start_date
while current_date <= end_date:
    # Format the date as a string in 'YYYY-MM-DD' format
    date_str = current_date.strftime('%Y-%m-%d')
    
    # Set URL parameters for the current date
    params = {'tidsperiod': 'ANNAN_PERIOD', 'tidsperiodFrom': date_str, 'tidsperiodTom': date_str,'amnesomradeId': '2', 'kungorelsetypId': '4', 'underRubrikId': '6'}
    
    try:
        # Send GET request with the current date
        response = requests.get(url, params=params)
        
        # Check if the request was successful
        if response.status_code == 200:
            try:
                # Try to parse the response as JSON
                data = response.json()
                # print(f"Data for {date_str}: {data}")
                
                # Save the data to a JSON file
                file_path = f'{date_str}.json'
                with open(file_path, 'w') as file:
                    json.dump(data, file, indent=4)
            except json.JSONDecodeError:
                # Handle cases where response is not valid JSON
                print(f"{date_str} ===== Response content is not valid JSON.")
                # print("Response text:", response.text)
                # Skip to the next iteration
                current_date += timedelta(days=1)
                continue
        else:
            print(f"Failed to retrieve data for {date_str}: {response.status_code}")
    
    except requests.RequestException as e:
        # Catch any request-related exceptions (e.g., network issues)
        print(f"Request failed for {date_str}: {str(e)}")
        # Skip to the next iteration
        continue
    
    # Move to the next day
    current_date += timedelta(days=1)
    
    # Sleep for 1 second to avoid overwhelming the server with requests
    time.sleep(1)
