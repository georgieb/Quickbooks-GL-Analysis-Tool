import csv
import pyodbc
conn = pyodbc.connect('DSN=QuickBooks Data;')
cursor = conn.cursor()
# test data
sql = """\
SELECT TxnDate, SalesLineItemRefFullName,SalesLineAmount FROM SalesLine
"""
rows = cursor.execute(sql)
with open(r'C:\Users\gborrero\documents\accountcsv.csv', 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow([x[0] for x in cursor.description])  # column headers
    for row in rows:
        writer.writerow(row)