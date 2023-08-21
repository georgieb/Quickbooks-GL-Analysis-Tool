
import pyodbc
conn = pyodbc.connect('DSN=QuickBooks Data;')
cursor = conn.cursor()
# test data
sql = """\
sp_report TxnListByDate show TxnType, Date, RefNumber, Name, Item, Quantity, Amount parameters DateFrom = {d '2018-01-01'}, DateTo = {d '2021-11-30'}
"""
rows = cursor.execute(sql)
with open(r'C:\Users\gborrero\documents\txnbydate.csv', 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow([x[0] for x in cursor.description])  # column headers
    for row in rows:
        writer.writerow(row)
