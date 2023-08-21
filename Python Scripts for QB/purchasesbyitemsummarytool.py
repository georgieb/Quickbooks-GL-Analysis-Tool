import csv
import pyodbc
conn = pyodbc.connect('DSN=QuickBooks Data;')
cursor = conn.cursor()
# test data
sql = """\
sp_report PurchasesByItemSummary show TxnType_Title, Date_Title, TxnId_Title, Item_Title, RefNumber_Title, Memo_Title, Name_Title, Quantity_Title, UnitPrice_Title, Amount_Title, RunningBalance_Title, Text, Blank, TxnType, Date, TxnID, Item, RefNumber, Memo, Name, Quantity, UnitPrice, Amount, RunningBalance parameters DateFrom = {d '2018-01-01'}
"""
rows = cursor.execute(sql)
with open(r'C:\Users\gborrero\documents\purchasesbyitemcsv.csv', 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow([x[0] for x in cursor.description])  # column headers
    for row in rows:
        writer.writerow(row)
