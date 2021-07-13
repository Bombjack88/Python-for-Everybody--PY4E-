import pyodbc

import pyodbc
conn = pyodbc.connect('Driver={SQL Server};'
                      'Server=sipo-dba06\wrap1;'
                      'Database=DL_DDEMC;'
                      'Trusted_Connection=yes";')

cursor = conn.cursor()
cursor.execute('SELECT TOP 100 * FROM DL_DDEMC.CQ.ComparacaoCRCEMF_CRCDetalhe order by Periodo')
for row in cursor:
    print(row[0],row[1])