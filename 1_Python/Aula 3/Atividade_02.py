"""
USE DB_SQL_GAMMA;

CREATE TABLE ATIVIDADE_02 
(
	ID					INT				NOT NULL IDENTITY(1, 1),
	ID_ORCAMENTO		VARCHAR(4)		NULL,
	ID_PROJETO			VARCHAR(4)		NULL,
	DATA				DATETIME        NULL,
	FATURAMENTO         DECIMAL(10, 2)	NULL,
	CONSTRAINT PK_ATIVIDADE_02 PRIMARY KEY (ID)
);
"""
import pyodbc
from datetime import datetime
from datetime import date

def execSQL(sql : str):
    cursor.execute(sql)
    insertObject = []
    columnNames = [column[0] for column in cursor.description]       
    for record in cursor.fetchall():
        insertObject.append( dict( zip( columnNames , record ) ) )

    return insertObject    

server = 'localhost'
database = 'DB_SQL_GAMMA'
username = 'sa'
password = '251x2mdlltfd'   
driver= '{SQL Server}'
connString = 'DRIVER='+driver+';SERVER='+server+';PORT=1433;DATABASE='+database+';UID='+username+';PWD='+ password

with open(r"DADOS_FATURAMENTO.txt",
          "r",
          encoding="latin1") as f:
    
    try:
        with pyodbc.connect(connString) as conn:
            with conn.cursor() as cursor:
                cursor.execute("DELETE FROM ATIVIDADE_02")
                cursor.commit()

                print (f"{datetime.now().strftime('%H:%M:%S')} Iniciando Carga")                    
                listData = []
                try:
                    for line in f:
                        dic = {}
                        dic["data"] = line[:8]
                        dic["orcamento"] = line[8:12]
                        dic["projeto"] = line[12:16]
                        dic["fatutamento"] = float(line[16:-1]) # por causa do \n
                        listData.append(dic)

                    print (f"{datetime.now().strftime('%H:%M:%S')} Carga Concluída")
                except Exception as e:
                    flog = open(r"LOG" + date.now().strftime('%Y%m%d')+".txt", "a+")
                    flog.write(f"Erro as {datetime.now().strftime('%H:%M:%S')} : \n Ao carregar o arquivo: {e} \n\n")
                    flog.close()

                print (f"{datetime.now().strftime('%H:%M:%S')} Iniciando Insert") 
                registroErro = []                   
                for item in listData:    
                    try:
                        cursor.execute("INSERT INTO ATIVIDADE_02(DATA, ID_ORCAMENTO, ID_PROJETO, FATURAMENTO) VALUES (?, ?, ?, ?)", 
                            item["data"][:4] + "-" + item["data"][4:6] + "-" + item["data"][6:], 
                            item["orcamento"], 
                            item["projeto"], 
                            item["fatutamento"])

                    except Exception as e:
                        cursor.execute("INSERT INTO LOG(DATA, DESCRICAO) VALUES (GETDATE(), ?)", 
                            f"Registro {item} erro {e}")

                cursor.commit()
                print(f"{datetime.now().strftime('%H:%M:%S')} Insert com sucesso" )
 
                if len(registroErro) > 0:
                    print(f"{datetime.now().strftime('%H:%M:%S')} Registros com erro")
                    fRegErro = open(r"registroErro.txt", "w+")
                    for rf in registroErro:
                        strEr += f"{rf['data']}" \
                                   f"{rf['orcamento']}" \
                                   f"{rf['projeto']}" \
                                   f"{rf['faturamento']}" \
                                   f"\n"      
                    fRegErro.write(strEr)
                    fRegErro.close()

    except Exception as e:
        flog = open(r"LOG" + date.today().strftime('%Y%m%d')+".txt", "a+")
        flog.write(f"Erro as {datetime.now().strftime('%H:%M:%S')} \n : Ao abrir o DB: {str(e)} \n\n")
        flog.close()

"""
with pyodbc.connect(connString) as conn:
    with conn.cursor() as cursor:

        insertObject = execSQL("SELECT * FROM ATIVIDADE_02 ORDER BY DATA")
        
for row in range(len(insertObject)):
    #print(insertObject[row])
    print(insertObject[row]['ID'], insertObject[row]['DATA'], insertObject[row]['ID_ORCAMENTO'], insertObject[row]['ID_PROJETO'], insertObject[row]['FATURAMENTO'])
"""