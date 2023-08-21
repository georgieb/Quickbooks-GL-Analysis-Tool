import csv
import pyodbc
conn = pyodbc.connect('DSN=QuickBooks Data;')
cursor = conn.cursor()
# test data
sql = """\
SELECT * FROM Transaction WHERE TxnDate >= {d '2018-01-01'}
"""
rows = cursor.execute(sql)


with open(r'C:\Users\gborrero\documents\transactionwheredateFY18.csv', 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow([x[0] for x in cursor.description])  # column headers
    for row in rows:
        writer.writerow(row)