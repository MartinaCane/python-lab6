import pymysql


def read_from_db():
    """
    Reading task list from a DB
    :return: a list of tasks
    """
    lista = list()
    # prepare the query for reading from DB
    query = "SELECT * FROM task"

    # connection to database
    connection = pymysql.connect(user="root", password="Matrix9697", host="localhost", database="first")

    # get a cursor
    cursor = connection.cursor()

    # execute query
    cursor.execute(query)

    # fetch result from query
    results = cursor.fetchall()

    # print(results)
    # x = dict()
    # print(x)

    # close cursor and connection
    cursor.close()
    connection.close()

    for result in results:
        temp = {'id': result[0], 'description': result[1], 'urgent': result[2]}
        lista.append(temp)

    return lista


def insert_new_task(description, urgent):
    query = "INSERT INTO task (description,urgent) VALUES (%s,%s)"

    # connectione to database
    connection = pymysql.connect(user="root", password="Matrix9697", host="localhost", database="first")
    cursor = connection.cursor()
    cursor.execute(query, (description, urgent))
    connection.commit()

    query = "SELECT * FROM task WHERE description=(%s)"
    cursor = connection.cursor()
    cursor.execute(query, (description,))
    connection.commit()
    result = cursor.fetchone()
    cursor.close()
    connection.close()
    temp = {'id': result[0], 'description': result[1], 'urgent': result[2]}

    return temp


def updating_Db(description, id):
    query = "UPDATE task SET description=(%s) WHERE id=(%s)"

    connection = pymysql.connect(user="root", password="Matrix9697", host="localhost", database="todolist")
    cursor = connection.cursor()
    cursor.execute(query, (description, id))
    connection.commit()
    cursor.close()
    connection.close()


def delete_task(id_task):
    query = "DELETE FROM task WHERE id=(%s)"

    # connectione to database
    connection = pymysql.connect(user="root", password="Matrix9697", host="localhost", database="first")

    cursor = connection.cursor()
    cursor.execute(query, (id_task,))
    connection.commit()
    cursor.close()
    connection.close()
