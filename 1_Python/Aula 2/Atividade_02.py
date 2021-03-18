"""
USE DB_SQL_GAMMA;

CREATE TABLE ATIVIDADE_02 
(
	ID					INT				NOT NULL IDENTITY(1, 1),
	ID_ORCAMENTO		INT				NOT NULL,
	ID_PROJETO			INT				NOT NULL,
	DATA				DATETIME        NOT NULL,
	FATURAMENTO         DECIMAL(10, 2)	NOT NULL,
	CONSTRAINT PK_ATIVIDADE_02 PRIMARY KEY (ID)
);
"""
import pyodbc

def procData(line):
    tmp = list(line)
    #print(tmp)
    _data = ''.join(tmp[0:8])
    _id_orcamento = int(''.join(tmp[9:13]))
    _id_projeto = int(''.join(tmp[14:17]))
    _faturamento = float(''.join(tmp[17:]))

    return _data, _id_orcamento, _id_projeto, _faturamento

server = 'localhost'
database = 'DB_SQL_GAMMA'
username = 'sa'
password = '251x2mdlltfd'   
driver= '{SQL Server}'


with open(r"DADOS_FATURAMENTO.txt",
          "r",
          encoding="latin1") as f:
    
    with pyodbc.connect('DRIVER='+driver+';SERVER='+server+';PORT=1433;DATABASE='+database+';UID='+username+';PWD='+ password) as conn:
        with conn.cursor() as cursor:
            cursor.execute("DELETE FROM ATIVIDADE_02")
            cursor.commit()

            try:
                for line in f:
                    _data, _id_orcamento, _id_projeto, _faturamento = procData(line)
                    #print(_data, _id_orcamento, _id_projeto, _faturamento)
                    cursor.execute("INSERT INTO ATIVIDADE_02(DATA, ID_ORCAMENTO, ID_PROJETO, FATURAMENTO) VALUES (?, ?, ?, ?)", _data, _id_orcamento, _id_projeto, _faturamento)
                    
                cursor.commit()
            except Exception as e:
                cursor.rollback()

with pyodbc.connect('DRIVER='+driver+';SERVER='+server+';PORT=1433;DATABASE='+database+';UID='+username+';PWD='+ password) as conn:
    with conn.cursor() as cursor:
        cursor.execute("SELECT * FROM ATIVIDADE_02")
        for row in cursor.fetchall():
            print(row)
