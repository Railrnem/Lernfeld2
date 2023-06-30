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

def addHardware(descr : str):
    db = connectDB()
    cursor = db.cursor()
    cursor.execute('INSERT INTO lernfeld2.hardware (bezeichnung) VALUES ("' + descr + '")')
    db.commit()
    cursor.close()
    db.close()

def addLaptop(descr : str, display : str,ram : str,storage : str,batteryhours : str):
    addHardware(descr)
    db = connectDB()
    cursor = db.cursor()
    # TODO: need to add foreign Key from Hardware
    cursor.execute('INSERT INTO lernfeld2.laptopeigenschaften (display,ram,storage,batteryhours) VALUES ("' + display + '","' + ram + '","' + storage + '","' + batteryhours + '")')
    db.commit()
    cursor.close()
    db.close()
    
    
def getLaptopHighScore(category: str):
    db = connectDB()
    cursor = db.cursor()
    cursor.execute(' \
        SELECT H.bezeichnung, H.id, E.id as Eid, S.id, S.'+ category + ' as Sid FROM hardware as H \
        INNER JOIN laptopeigenschaften as E ON H.id = E.laptopid \
        INNER JOIN laptopscore as S ON S.id = E.id \
        ORDER BY S.'+ category +' DESC \
        LIMIT 3; \
    ')
    result = cursor.fetchall()
    return result