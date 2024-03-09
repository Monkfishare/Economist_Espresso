import json
import requests

url = "https://www.economist.com/the-world-in-brief"

# Send a GET request to the URL
response = requests.get(url)

# Check if the request was successful (status code 200)
if response.status_code == 200:
    # Extract the JSON data from the HTML response
    start_index = response.text.find('<script type="application/ld+json">') + len('<script type="application/ld+json">')
    end_index = response.text.find('</script>', start_index)
    json_data = response.text[start_index:end_index].strip()

    # Parse the JSON data
    data = json.loads(json_data)

    # Extract datePublished and dateModified
    date_published = data.get("datePublished", "")
    date_modified = data.get("dateModified", "")

    # Print the results
    print("Date Published:", date_published)
    print("Date Modified:", date_modified)

    # Save the values to text files
    with open("DatePublished.txt", "w") as file_published:
        file_published.write(date_published)

    with open("DateModified.txt", "w") as file_modified:
        file_modified.write(date_modified)

    print("Date Published saved to 'DatePublished.txt'")
    print("Date Modified saved to 'DateModified.txt'")
else:
    print("Failed to fetch data. Status code:", response.status_code)
