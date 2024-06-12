import csv
import requests

API_KEY = '20e102eb75104a328eed75291b8c5faa'
input_file = 'hosts_addresses.csv'
output_file = 'hosts_geolocation.csv'

def geocode_address(address):
    url = f'https://api.opencagedata.com/geocode/v1/json?q={address}&key={API_KEY}'
    response = requests.get(url).json()
    if response['results']:
        geometry = response['results'][0]['geometry']
        return geometry['lat'], geometry['lng']
    else:
        return None, None

with open(input_file, mode='r') as infile, open(output_file, mode='w', newline='') as outfile:
    reader = csv.DictReader(infile)
    fieldnames = reader.fieldnames + ['latitude', 'longitude']
    writer = csv.DictWriter(outfile, fieldnames=fieldnames)

    writer.writeheader()
    for row in reader:
        lat, lon = geocode_address(row['address'])
        row['latitude'] = lat
        row['longitude'] = lon
        writer.writerow(row)

print(f'Geolocation data has been written to {output_file}')
