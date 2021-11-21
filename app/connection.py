import mysql.connector
def insert_bd(nome, operacao):
    try:
        mydb = mysql.connector.connect(
            user = "userApp",
            database = "musica",
            password = "urubu100",
            host = "localhost"
        )

        if mydb.is_connected():
            print("A conexão foi aberta")
            mycursor = mydb.cursor()
            if operacao == 1:
                sql_query = "INSERT INTO musica(nomeMusica) VALUES (%s)"
            elif operacao == 2:
                sql_query = "INSERT INTO artista(nome) VALUES (%s)"
            elif operacao == 3:
                sql_query = "INSERT INTO musica(nomeMusica) VALUES (%s)"

            val = [nome]
            mycursor.execute(sql_query, val)

            mydb.commit()

    except mysql.connector.Error as e:
            print("Erro ao conectar com o MySQL", e)
    finally:
        if(mydb.is_connected()):
            mycursor.close()
            mydb.close()
            print("Conexão com MySQL está fechada\n")

def selectArtistas():
    mydb = mysql.connector.connect(
            user = "userApp",
            database = "musica",
            password = "urubu100",
            host = "localhost"
        )

    sql_select_Query = "select * from artista"
    cursor = mydb.cursor()
    cursor.execute(sql_select_Query)
    # get all records
    records = cursor.fetchall()
    # print("Total number of rows in table: ", cursor.rowcount)

    print("\nArtistas")
    for row in records:
        print("Id = ", row[0], "- Nome = ", row[1])
    print("\n")

def selectLastMusic():
    mydb = mysql.connector.connect(
            user = "userApp",
            database = "musica",
            password = "urubu100",
            host = "localhost"
        )

    sql_select_Query = "select idMusica from musica order by idMusica desc limit 1"
    cursor = mydb.cursor()
    cursor.execute(sql_select_Query)
    # get all records
    records = cursor.fetchall()
    # print("Total number of rows in table: ", cursor.rowcount)

    return records[0][0]

def associarArtMusica(art, mus):
    print(f"ID ÚLTIMA MUSICA: {mus}")
    try:
        mydb = mysql.connector.connect(
            user = "userApp",
            database = "musica",
            password = "urubu100",
            host = "localhost"
        )

        if mydb.is_connected():
            print("A conexão foi aberta - associação")
            mycursor = mydb.cursor()
            sql_query = ""

            musica = mus
            artista = art
            for record in artista:  
                mycursor = mydb.cursor()
                mycursor.execute(f"INSERT INTO musica_artista VALUES ({musica} , {record})")
                mydb.commit()


    except mysql.connector.Error as e:
        print("Erro ao conectar com o MySQL", e)
    finally:
        if(mydb.is_connected()):
            mycursor.close()
            mydb.close()
            print("Conexão com MySQL está fechada\n")
