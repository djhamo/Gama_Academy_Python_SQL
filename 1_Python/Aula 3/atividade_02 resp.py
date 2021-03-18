import pyodbc
from datetime import date, datetime

with open(r"C:\Arquivos\DADOS_FATURAMENTO.txt", "r",
          encoding="latin1") as f:
    try:
        conn = pyodbc.connect("Driver={SQL Server};"
                              "Server=LOCALHOST;"
                              "Database=DB_FINANCEIRO;"
                              "UID=sa;"
                              "PWD=sa;")
        cursor = conn.cursor()

        print(f"{datetime.now().strftime('%H:%M:%S')}: "
              f"Carga de dados iniciada...")
        listData = []
        for line in f:
            dic = {}
            dic["data"] = line[:8]
            dic["orcamento"] = line[8:12]
            dic["projeto"] = line[12:16]
            dic["faturamento"] = float(line[16:-1])
            listData.append(dic)

        print(f"{datetime.now().strftime('%H:%M:%S')}: "
              f"Carga de dados concluída...")
        print(f"{datetime.now().strftime('%H:%M:%S')}: "
              f"Inserção na base de dados iniciada...")

        registrosComErro = []
        for item in listData:
            try:
                cursor.execute("INSERT INTO DADOS_FATURAMENTO VALUES (?, ?, ?, ?)",
                               item["orcamento"],
                               item["projeto"],
                               item["faturamento"],
                               item["data"][:4] + "-" + item["data"][4:6] + "-" + item["data"][6:])
            except Exception as e:
                registrosComErro.append(item)
                #Função SQL Server para escrever data e hora: GETDATE()
                #Função MySQl para escrever data e hora: Now()
                cursor.execute("INSERT INTO Log VALUES (GETDATE(), ?)",
                               f"Registro que originou o problema: {item}."
                               f" Informações Técnicas: {str(e)}")

        conn.commit()
        print(f"{datetime.now().strftime('%H:%M:%S')}: "
              f"Inserção concluída com sucesso...")
                
        if len(registrosComErro) > 0:
            fRegistrosErro = open(r"C:\Arquivos\registrosErro.txt", "w+")
            strRegistrosErro = ""
            for registroErro in registrosComErro:
                strRegistrosErro += f"{registroErro['data']}" \
                                    f"{registroErro['orcamento']}" \
                                    f"{registroErro['projeto']}" \
                                    f"{registroErro['faturamento']}\n"
            fRegistrosErro.write(strRegistrosErro)
            fRegistrosErro.close()

    except Exception as e:
        print(f"Erro na execução: \n {str(e)}")
        fLog = open(r"C:\Arquivos\LOG_"
                    + date.today().strftime('%Y%m%d') +
                    ".txt", "a+")
        fLog.write(f"Erro as {datetime.now().strftime('%H:%M:%S')}: \n"
                   f"{str(e)} \n\n")
        fLog.close()

