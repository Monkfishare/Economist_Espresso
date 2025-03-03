import json
import requests

url = "https://www.economist.com/the-world-in-brief"

response = requests.get(url)

if response.status_code == 200:
    start_index = response.text.find('<script type="application/ld+json">') + len('<script type="application/ld+json">')
    end_index = response.text.find('</script>', start_index)
    json_data = response.text[start_index:end_index].strip()
    data = json.loads(json_data)
    date_published = data.get("datePublished", "")
    date_modified = data.get("dateModified", "")

    print("Date Published:", date_published)
    print("Date Modified:", date_modified)

    with open("DatePublished.txt", "w") as file_published:
        file_published.write(date_published)

    with open("DateModified.txt", "w") as file_modified:
        file_modified.write(date_modified)

    print("Date Published saved to 'DatePublished.txt'")
    print("Date Modified saved to 'DateModified.txt'")
else:
    print("Failed to fetch data. Status code:", response.status_code)
