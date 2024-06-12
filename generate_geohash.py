import csv
import geohash

input_file = 'hosts_geolocation.csv'
output_file = 'hosts_geolocation_with_geohash.csv'

with open(input_file, mode='r') as infile, open(output_file, mode='w', newline='') as outfile:
    reader = csv.DictReader(infile)
    fieldnames = reader.fieldnames + ['geohash']
    writer = csv.DictWriter(outfile, fieldnames=fieldnames)

    writer.writeheader()
    for row in reader:
        latitude = float(row['latitude'])
        longitude = float(row['longitude'])
        row['geohash'] = geohash.encode(latitude, longitude)
        writer.writerow(row)

print(f'GeoHash values have been written to {output_file}')
