import pymysql


def read_from_db():
    """
    Reading task list from a DB
    :return: a list of tasks
    """
    lista = list()
    # prepare the query for reading from DB
    query = "SELECT * FROM task"

    # connectione to database
    connection = pymysql.connect(user="root", password="Matrix9697", host="localhost", database="first")

    # get a cursor
    cursor = connection.cursor()

    # execute query
    cursor.execute(query)

    # fetch result from query
    results = cursor.fetchall()
    print(results)
    x = dict()
    print(x)

    # close cursor and connection
    cursor.close()
    connection.close()
    return results
