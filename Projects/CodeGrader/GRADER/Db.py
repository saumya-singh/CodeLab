import MySQLdb
import traceback

class Db:
    
    def getConnection(self):
        connection = MySQLdb.connect(host="192.168.43.190", user="root", passwd="1234", db="userlogin")
        return connection

    def executeQuery(self, query):
        connection = self.getConnection()
        cursor = connection.cursor()
        try:
            cursor.execute(query)
            result = cursor.fetchall()
            connection.commit()
            connection.close()
            return result

        except:
            traceback.print_exc()
            print "Error: unable to fetch data"


if __name__ == "__main__":
    db = Db()
    query = "SELECT submission_id, file_name FROM submissions WHERE status='pending' ORDER BY time_of_submission ASC LIMIT 1"
    print db.executeQuery(query)
    