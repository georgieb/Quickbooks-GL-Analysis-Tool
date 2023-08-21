import csv
import pyodbc
conn = pyodbc.connect('DSN=QuickBooks Data;')
cursor = conn.cursor()
# test data
sql = """\
sp_report TxnListByDate show Text, TxnType, Date, Item, RefNumber, Name, Memo, Account, SplitAccount, Quantity, Debit, Credit, Amount parameters DateFrom = {d '2018-01-01'}, DateTo = {d '2021-12-31'}
"""
rows = cursor.execute(sql)
with open(r'C:\Users\gborrero\documents\txnbydateFY18-FY21.csv', 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow([x[0] for x in cursor.description])  # column headers
    for row in rows:
        writer.writerow(row)
