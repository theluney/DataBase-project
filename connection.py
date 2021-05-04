import cx_Oracle

connection = cx_Oracle.connect("DB_PROJECT", 'pass', "localhost:1521/xe", encoding="UTF-8")
c = connection.cursor()