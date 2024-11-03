import sqlite3
import csv

print("Customer Data Importer\n")

csv_file_path = 'customers.csv'
db_file_path = 'customers.sqlite'

conn = sqlite3.connect(db_file_path)
cursor = conn.cursor()

create_table_query = '''
CREATE TABLE IF NOT EXISTS Customer (
    customerID INTEGER PRIMARY KEY,
    firstName TEXT,
    lastName TEXT,
    companyName TEXT,
    address TEXT,
    city TEXT,
    state TEXT,
    zip TEXT
)
'''

cursor.execute(create_table_query)

cursor.execute('DELETE FROM Customer')
print("All old rows deleted from Customer table.")

with open(csv_file_path, 'r') as csvfile:
    csv_reader = csv.DictReader(csvfile)
    rows = [(row['first_name'], row['last_name'], row['company_name'], row['address'], row['city'], row['state'], row['zip']) for row in csv_reader]
    
    insert_query = '''
    INSERT INTO Customer (firstName, lastName, companyName, address, city, state, zip)
    VALUES (?, ?, ?, ?, ?, ?, ?)
    '''
    
    cursor.executemany(insert_query, rows)
    print(f"{len(rows)} row(s) inserted into Customer table.")

conn.commit()
conn.close()
