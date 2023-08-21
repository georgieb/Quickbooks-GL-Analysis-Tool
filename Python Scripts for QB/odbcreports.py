import csv
import pyodbc
conn = pyodbc.connect('DSN=QuickBooks Data;')
cursor = conn.cursor()
# test data
sql = """\
sp_report ProfitAndLossStandard show Text, Label, Amount_1_Title as Month_1, Amount_1,
      Amount_2_Title as Month_2, Amount_2, Amount_3_Title as Month_3, Amount_3,
      Amount_4_Title as Month_4, Amount_4, Amount_5_Title as Month_5, Amount_5,
      Amount_6_Title as Month_6, Amount_6, Amount_7_Title as Month_7, Amount_7,
      Amount_8_Title as Month_8, Amount_8, Amount_9_Title as Month_9, Amount_9,
      Amount_10_Title as Month_10, Amount_10, Amount_11_Title as Month_11, Amount_11,
      Amount_12_Title as Month_12, Amount_12, Amount_13_Title as Total, Amount_13 as Total_Amount
      parameters DateMacro = 'ThisYear', SummarizeColumnsBy = 'Month'
"""
rows = cursor.execute(sql)
with open(r'C:\Users\gborrero\documents\odbccsv2.csv', 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow([x[0] for x in cursor.description])  # column headers
    for row in rows:
        writer.writerow(row)

