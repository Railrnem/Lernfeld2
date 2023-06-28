import mysql.connector

# Connection-Details
host="localhost"
user="root"
password="1998"
database="lernfeld2"
port=3307

# Establish db-connection
def connectDB():
    return mysql.connector.connect(host=host, user=user, password=password, database=database, port=port)

# Print Laptop from database
def printLaptop():
    db = connectDB()
    cursor = db.cursor()
    cursor.execute("""
        SELECT bezeichnung FROM lernfeld2.hardware
    """)
    result = cursor.fetchall()
    return result

def addHardware(descr : str, prop : str, typ : str):
    db = connectDB()
    cursor = db.cursor()
    cursor.execute('INSERT INTO lernfeld2.hardware (bezeichnung, eigenschaften, typ) VALUES ("' + descr + '",' + str(prop) + ' ,"' + typ + '")')
    db.commit()
    cursor.close()
    db.close()
    