import mysql.connector

class Database():
    # Connection-Details
    host="localhost"
    user="root"
    password="1998"
    database="lernfeld2"
    port=3306

    # Establish db-connection
    def connectDB(self):
        return mysql.connector.connect(host=self.host, user=self.user, password=self.password, database=self.database, port=self.port)
        
    # Returns a list of the best 3 Laptops according to the category given
    def getLaptopHighScore(self, category: str):
        db = self.connectDB()
        cursor = db.cursor()
        cursor.execute(' \
            SELECT H.bezeichnung, E.display, E.ram, E.storage, E.batteryhours FROM hardware as H \
            INNER JOIN laptopeigenschaften as E ON H.id = E.laptopid \
            INNER JOIN laptopscore as S ON S.id = E.id \
            ORDER BY S.'+ category +' DESC \
            LIMIT 3; \
        ')
        result = cursor.fetchall()
        cursor.close()
        db.close()
        return result
        
    # Returns a list of the best 3 Comnputers according to the category given
    def getComputerHighScore(self, category: str):
        db = self.connectDB()
        cursor = db.cursor()
        cursor.execute(' \
            SELECT H.bezeichnung, E.cpu, E.gpu, E.ram, E.storage FROM hardware as H \
            INNER JOIN computereigenschaften as E ON H.id = E.computerid \
            INNER JOIN computerscore as S ON S.id = E.id \
            ORDER BY S.'+ category +' DESC \
            LIMIT 3; \
        ')
        result = cursor.fetchall()
        cursor.close()
        db.close()
        return result