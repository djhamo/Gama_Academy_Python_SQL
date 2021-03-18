import requests
import pyodbc
from datetime import datetime
from datetime import date

connString = 'DRIVER='+driver+';SERVER='+server+';PORT=1433;DATABASE='+database+';UID='+username+';PWD='+ password
#print(connString)

def execSQL(sql : str, cursor):
    cursor.execute(sql)
    insertObject = []
    columnNames = [column[0] for column in cursor.description]       
    for record in cursor.fetchall():
        insertObject.append( dict( zip( columnNames , record ) ) )

    return insertObject    

def limpaTudo():
    print(f"{datetime.now().strftime('%H:%M:%S')} Limpando TUDO")
    try:
        with pyodbc.connect(connString) as conn:
            with conn.cursor() as cursor:
                cursor.execute("DELETE FROM DISTRITO")
                cursor.execute("DELETE FROM CIDADE")
                cursor.execute("DELETE FROM UF")
                cursor.execute("DELETE FROM REGIAO")
                cursor.commit()
    except Exception as e:
        print(f"{datetime.now().strftime('%H:%M:%S')} Erro ao Limpar DB{e}")

def mostraDistrito():
    with pyodbc.connect(connString) as conn:
        with conn.cursor() as cursor:
            insertObject = execSQL("SELECT * FROM DISTRITO", cursor)
            
    for row in range(len(insertObject)):
        #print(insertObject[row])
        print(datetime.now().strftime('%H:%M:%S'), insertObject[row]['ID'], insertObject[row]['NOME'], insertObject[row]['ID_CIDADE'])


def carregaURLDB(url: str, sql : str, campos : dict, table : str, id_pai : int = 0):
    #print(url)
    #print(sql)
    #print(connString)
    #print(campos)
    #print(id_pai)
    #print(table)
    print(f"{datetime.now().strftime('%H:%M:%S')} Processando {table}")

    try:
        with requests.get(url) as res:
            json = res.json()
            #print(json)
            try:
                with pyodbc.connect(connString) as conn:
                    with conn.cursor() as cursor:
                        cursor.execute(f"SET IDENTITY_INSERT {table} ON")
                        val = []
                        try:
                            for item in json:
                                temp = []
                                for valor in campos.values():
                                    if type(valor) != list:
                                        #print(f"{valor} => ({item[valor]})")
                                        temp.append(item[valor])
                                    else:
                                        x = item.copy()
                                        for tt in range(len(valor)):
                                            x = x.get(valor[tt])   
                                        #print(f" ({x})")
                                        temp.append(x)
                                
                                if id_pai != 0:
                                    temp.append(id_pai)
                                
                                #print(temp)
                                val.append(temp)
                            #print(val)
                        except Exception as e:
                            print(f"{datetime.now().strftime('%H:%M:%S')} Montagem do VAL {e}")

                        try:
                            cursor.executemany(sql, val)

                        except Exception as e:
                            print(f"{datetime.now().strftime('%H:%M:%S')} Erro no inserir {e}")
                            #cursor.execute("INSERT INTO LOG(DATA, DESCRICAO) VALUES (GETDATE(), ?)", 
                            #    f"Registro {item} erro {e}")

                        
                        cursor.commit()
                        cursor.execute(f"SET IDENTITY_INSERT {table} OFF")
                    
            except Exception as e:
                print(f"{datetime.now().strftime('%H:%M:%S')} Erro no connect do banco {e}")

    except Exception as e:
        print(f"{datetime.now().strftime('%H:%M:%S')} Erro no GET IBGE{e}")

    print(f"{datetime.now().strftime('%H:%M:%S')} {table} Finalizado")


def carregaIBGE2():
    carregaURLDB('https://servicodados.ibge.gov.br/api/v1/localidades/regioes', 
        "INSERT INTO REGIAO(ID, NOME, SIGLA) VALUES (?, ?, ?)", 
        {"ID" :'id', "NOME": 'nome', "SIGLA": 'sigla'},
        'REGIAO')
    
    carregaURLDB('https://servicodados.ibge.gov.br/api/v1/localidades/estados', 
        "INSERT INTO UF(ID, NOME, SIGLA, ID_REGIAO) VALUES (?, ?, ?, ?)",
        {"ID" :'id', "NOME": 'nome', "SIGLA": 'sigla', "ID_REGIAO": ["regiao", "id"]},
        'UF')

    carregaURLDB(f'https://servicodados.ibge.gov.br/api/v1/localidades/municipios', 
        "INSERT INTO CIDADE(ID, NOME, ID_UF) VALUES (?, ?, ?)",
        {"ID" :'id', "NOME": 'nome', "ID_UF": ["microrregiao", "mesorregiao", "UF", "id"]},
        'CIDADE')

    carregaURLDB(f'https://servicodados.ibge.gov.br/api/v1/localidades/distritos', 
        "INSERT INTO DISTRITO(ID, NOME, ID_CIDADE) VALUES (?, ?, ?)",
        {"ID" :'id', "NOME": 'nome', "ID_CIDADE": ["municipio", "id"]},
        'DISTRITO')

def criaTable():
    print(f"{datetime.now().strftime('%H:%M:%S')} Criando Estrutura")

    try:
        with pyodbc.connect(connString) as conn:
            with conn.cursor() as cursor:
                cursor.execute(
                    "CREATE TABLE REGIAO" \
                        "(" \
                            "ID 				INT				NOT NULL IDENTITY(1, 1)," \
	                        "NOME				VARCHAR(50)		NOT NULL, " \
	                        "SIGLA				VARCHAR(2)		NOT NULL," \
	                            "CONSTRAINT PK_REGIAO PRIMARY KEY (ID)" \
                        ")"
                    )
                cursor.execute(
                    "CREATE TABLE UF" \
                        "(" \
                            "ID 				INT				NOT NULL IDENTITY(1, 1)," \
                            "ID_REGIAO			INT				NOT NULL," \
                            "NOME				VARCHAR(50)		NOT NULL," \
                            "SIGLA				VARCHAR(2)		NOT NULL," \
                            "CONSTRAINT PK_UF PRIMARY KEY (ID)," \
                            "CONSTRAINT FK_UF_REGIAO FOREIGN KEY (ID_REGIAO)" \
                                "REFERENCES REGIAO (ID)" \
                        ")"
                    )
                cursor.execute(
                    "CREATE TABLE CIDADE" \
                        "(" \
                            "ID 				INT				NOT NULL IDENTITY(1, 1)," \
                            "ID_UF				INT				NOT NULL," \
                            "NOME				VARCHAR(50)		NOT NULL," \
                            "CONSTRAINT PK_CIDADE PRIMARY KEY (ID)," \
                            "CONSTRAINT FK_CIDADE_UF FOREIGN KEY (ID_UF)" \
                                "REFERENCES UF (ID)	" \
                        ")"
                    )
                cursor.execute(
                    "CREATE TABLE DISTRITO" \
                        "(" \
                            "ID 				INT				NOT NULL IDENTITY(1, 1)," \
                            "ID_CIDADE			INT				NOT NULL," \
                            "NOME				VARCHAR(50)		NOT NULL," \
                            "CONSTRAINT PK_DISTRITO PRIMARY KEY (ID)," \
                            "CONSTRAINT FK_DISTRITO_CIDADE FOREIGN KEY (ID_CIDADE)" \
                                "REFERENCES CIDADE (ID)	" \
                        ")"
                    )
                cursor.commit()
    except Exception as e:
        print(f"{datetime.now().strftime('%H:%M:%S')} Erro ao Criar DB{e}")



def recebeOpcaoUsuario():
    opcao = 0

    print("Digite a opção que deseja executar:\n"
          "1 - Carrega dados do IBGE\n"
          "2 - Limpa Base Azure\n"
          "3 - Imprimir Todos Distritos\n"
          "4 - Cria estrutura do DB\n"
          "5 - Sair do Programa\n")

    while opcao < 1 or opcao > 5:
        opcao = int(input("Digite uma opção válida (1 - 5): "))
        if opcao < 1 or opcao > 5:
            print("Opção inválida. Digite novamente")

    return opcao

if __name__ == '__main__':
    opcao = recebeOpcaoUsuario()

    while opcao >= 1 and opcao <= 4:
        if opcao == 1: #Carregar Dados do IBGE
            print("Opção 1 - Carrega dados do IBGE\n")            
            carregaIBGE2()

        elif opcao == 2: #Limpa Base
            print("Opção2 - Limpa Base Azure")
            limpaTudo()

        elif opcao == 3: #Imprimir Todos Distritos
            print("Opção3 - Imprimir Todos Distritos")
            mostraDistrito()

        elif opcao == 4: #Cria DB
            print("Opção4 - Cria estrutura DB")
            criaTable()

        else: #sair do programa
            print("Você saiu do programa. Obrigado por usar...\n")
            opcao = 5

        if opcao != 5:
            opcao = recebeOpcaoUsuario()

