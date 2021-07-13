import sqlite3

# open in two steps
conn = sqlite3.connect('emaildb.sqlite') #cria o ficheiro na diretoria do programa
cur = conn.cursor() #uma espécie de handle

cur.execute('DROP TABLE IF EXISTS Counts') #drop the table se existir

cur.execute('''
CREATE TABLE Counts (email TEXT, count INTEGER)''')

fname = input('Enter file name: ')
if (len(fname) < 1): fname = 'mbox-short.txt'
fh = open(fname)
for line in fh:
    if not line.startswith('From: '): continue
    pieces = line.split()
    email = pieces[1]
    cur.execute('SELECT count FROM Counts WHERE email = ? ', (email,))      #vai substituir o ? pelo email
    row = cur.fetchone()                                                    #refere-se à primeira linha da base de dados
    if row is None:                               #se ainda não existir qualquer registo ele acrescenta o email e coloca o número 1 no count
        cur.execute('''INSERT INTO Counts (email, count)
                VALUES (?, 1)''', (email,))
    else:
        cur.execute('UPDATE Counts SET count = count + 1 WHERE email = ?',
                    (email,))
    conn.commit() #escrever na base de dados os resultados, opção de fazer a cada loop, mas poderia ser a cada 10 loops por exemplo

# https://www.sqlite.org/lang_select.html
sqlstr = 'SELECT email, count FROM Counts ORDER BY count DESC LIMIT 10'

for row in cur.execute(sqlstr):
    print(str(row[0]), row[1])

cur.close()
