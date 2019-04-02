import psycopg2

class postgres_UUID:
    def __init__(self, filename, filepath, key_uuid):
        self.filename = filename
        self.filepath = filepath
        self.key_uuid = key_uuid
        self.public_keyring = None
        self.passphrase = None
    #first process for picking up the newly provided keyring and passing it to the main class
    def getPost(self):
        pinfo = [self.public_keyring, self.passphrase]
        return pinfo
    def setPost(self, public_keyring, passphrase):
        self.public_keyring = public_keyring
        self.passphrase = passphrase
    def post_connect(self):
        #connect to the poper data base above
            conn = psycopg2.connect(database="dvdrental", user = "postgres", password = "pass123", host = "127.0.0.1", port = "5432")

    def querying_data(self, key_uuid, conn):
        #Cursor is need to avoid memory overrun, selecting one query. 
        cur = conn.cursor()
        #running normal SQL calls here. the %s is important if you are needing to specify something from a list. Must be an int.
        cur.execute("SELECT * FROM keys WHERE key_uuid = ANY(%s);", (key_uuid,))
        rows = cur.fetchall()
        public_keyring.clear()
        location_encryped_file.clear()
        passphrase = 'loopyloom.'
        #call the needed item and put it into a list
        for row in rows:
           public_keyring=(row[0])
        #   location_encryped_file = (row[1])
        #   passphrase=(row[1])
        #   print "SECRET-KEY = ", row[3], 
        #   print "PRIVATE-KEY = ",row [4], "\n"
        print ("Operation done successfully");
        conn.close()
        self.setPost(public_keyring, passphrase)
        return self.getPost()
#postgres_UUID()
