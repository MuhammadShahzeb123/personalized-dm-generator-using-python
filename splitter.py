import unicodecsv as csv

INPUT_FILE = 'lead.csv'
ROWS_PER_FILE = 100

with open(INPUT_FILE, 'rb') as infile:
    reader = csv.reader(infile)
    header = next(reader)  # Read the header row
    rows = list(reader)

total_files = len(rows) // ROWS_PER_FILE + 1  # Calculate total number of files

for i in range(total_files):
    file_name = f'lead-{i+1}.csv'
    with open(file_name, 'wb') as outfile:
        writer = csv.writer(outfile)
        writer.writerow(header)  # Write the header to each file
        start_index = i * ROWS_PER_FILE
        end_index = min((i + 1) * ROWS_PER_FILE, len(rows))
        writer.writerows(rows[start_index:end_index])
