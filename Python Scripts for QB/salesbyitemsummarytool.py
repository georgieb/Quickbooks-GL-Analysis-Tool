import csv
import pyodbc
conn = pyodbc.connect('DSN=QuickBooks Data;')
cursor = conn.cursor()
# test data
sql = """\
sp_report SalesByItemSummary show Quantity_Title, Amount_Title, Percent_Title, AveragePrice_Title, AmountCOGS_Title, AmountAvgCOGS_Title, AmountGrossMargin_Title, PercentGrossMargin_Title, Text, Label, Quantity, Amount, Percent, AveragePrice, AmountCOGS, AmountAvgCOGS, AmountCOGS, AmountGrossMargin, PercentGrossMargin parameters DateFrom = {d '2018-01-01'}, DateTo = {d '2021-11-30'}, SummarizeColumnsBy = 'Month' 
"""
rows = cursor.execute(sql)
with open(r'C:\Users\gborrero\documents\salesbyitemsummary.csv', 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow([x[0] for x in cursor.description])  # column headers
    for row in rows:
        writer.writerow(row)