import mysql.connector

# Connection-Details
host="localhost"
user="root"
password="1998"
database="lernfeld2"
port=3307

# Establish db-connection
db=mysql.connector.connect(host=host, user=user, password=password, database=database, port=port)

print("Was für eine Hardware brauchst du?")
print("Mögliche Eingaben: Laptop")

selection = input()

if(isinstance(selection, str)):
    if(selection == "Laptop"):
        cursor = db.cursor()
        cursor.execute("""
            SELECT bezeichnung FROM lernfeld2.hardware
        """)
        result = cursor.fetchall()
        print(result)
else:
    print("Ungültige Eingabe")
