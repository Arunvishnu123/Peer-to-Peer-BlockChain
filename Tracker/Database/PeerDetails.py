import sqlite3

class PeerDetailsTable:
    def __init__(self):
        pass

    def createTable(self):
        db = sqlite3.connect('./Tracker/DatabaseSource/BlockChain.db')
        try:
            cur = db.cursor()
            cur.execute('''CREATE TABLE peerData (
            peerName TEXT (20) NOT NULL,
            peerPublicKey TEXT (20) NOT NULL,
            peerIPAddress TEXT (20) NOT NULL,
            peerPort INTEGER);''')
            print('table created successfully')
        except:
            print('error in operation')
            db.rollback()
        db.close()

    def addElements(self,data):
        db = sqlite3.connect('./Tracker/DatabaseSource/BlockChain.db')
        qry = "insert into peerData (peerName, peerPublicKey,peerIPAddress,peerPort) values(?,?,?,?);"
        try:
            cur = db.cursor()
            cur.execute(qry, data)
            db.commit()
            print("new peer details added to the database successfully")
        except:
            print("error in operation")
            db.rollback()
        db.close()

    #retrive all ipaddress and port number
    def retrieveElements(self):
        db = sqlite3.connect('./Tracker/DatabaseSource/BlockChain.db')
        qry = """select peerIPAddress , peerPort FROM peerData """
        try:
            cur = db.cursor()
            cur.execute(qry)
            result = cur.fetchall()
            cur.close()
            return result
        except:
            print("error in operation")

    def retreievePeerName(self):
        db = sqlite3.connect('./Tracker/DatabaseSource/BlockChain.db')
        qry = """select peerName FROM peerData """
        try:
            cur = db.cursor()
            cur.execute(qry)
            result = cur.fetchall()
            cur.close()
            return result
        except:
            print("error in operation")


    def retrieveAllSelected(self,name):
        db = sqlite3.connect('./Tracker/DatabaseSource/BlockChain.db')
        qry = """select * FROM peerData where peerName = ? """
        try:
            cur = db.cursor()
            cur.execute(qry,(name,))
            result = cur.fetchone()
            cur.close()
            return result
        except:
            print("error in operation")

    def deletePeerData(self,name):
        db = sqlite3.connect('./Tracker/DatabaseSource/BlockChain.db')
        qry = """select * FROM peerData where peerName = ? """
        try:
            cur = db.cursor()
            cur.execute(qry,(name,))
            cur.commit()
            cur.close()
        except:
            print("error in operation")


