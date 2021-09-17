from getpass import getpass
from mysql.connector import connect, Error

CreateDB = '''CREATE TABLE CUSTOMERS(
                id INT PRIMARY KEY NOT NULL AUTO_INCREMENT,
                Name TEXT NOT NULL,
                NumberUC VARCHAR(255) NOT NULL,
                Localization VARCHAR(500) NOT NULL,
                CEP VARCHAR(40) NOT NULL,
                District VARCHAR(500) NOT NULL, 
                Email VARCHAR(255) NOT NULL,
                Phone VARCHAR(50) NOT NULL,
                CPF_CNPJ VARCHAR(75) NOT NULL, 
                Payment VARCHAR(500),
                NOTES TEXT);'''
CreateTesteDB = '''INSERT INTO CUSTOMERS (Name, NumberUC, Localization, CEP, District, Email, Phone, CPF_CNPJ, Payment, NOTES) 
                VALUES ('Leonardo Felipe', '000001', 'Rua Daltro Filho', '98801-510', 'Centro', 'Leonardo@teste', '(55)99992-1300', '000.000.000-01', 'Entrada: 5000, Finalização: 3000', 'TEXTO DE OBSERVAÇÕES.')'''

def ConectBD():
        try:
                with connect(
                        host="localhost",
                        user="test",
                        password='12345678',
                        database='ordemservicosenergensteste',
                ) as connection:
                        with connection.cursor() as cursor:
                                cursor.execute(CreateDB)
                                cursor.execute(CreateTesteDB)
                                connection.commit()
        except Error as e:
                print(e)



## Name, NumberUC, Localization, CEP, District, Email, Phone, CPF_CNPJ, Payment, NOTES
def InsertBD():
        cur.execute("INSERT INTO CUSTOMERS (Name, NumberUC, Localization, CEP, District, Email, Phone, CPF_CNPJ, Payment, NOTES) VALUES ('Leonardo Felipe', '000001', 'Rua Daltro Filho', '98801-510', 'Centro', 'Leonardo@teste', '(55)99992-1300', '000.000.000-01', 'Entrada: 5000, Finalização: 3000', 'TEXTO DE OBSERVAÇÕES.')")
ConectBD()