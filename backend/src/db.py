import psycopg2 as db

class Config:

    def __init__(self):
        self.config = {
            "postgres": {
                "user": "postgres",
                "password": "eib",
                "host": "localhost",
                "port": "5432",
                "database": "saojose"
            }
        }

class Connection(Config):
    def __init__(self):
        Config.__init__(self)

        try:
            self.conn = db.connect(**self.config["postgres"])
            self.cur = self.conn.cursor()
        except Exception as e:
            print('Connection error. ', e)

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.commit
        self.connection.close()

    @property
    def connection(self):
        return self.conn
    
    @property
    def cursor(self):
        return self.cur
    
    def commit(self):
        return self.conn.commit()

    def fetchall(self):
        return self.cursor.fetchall()

    def execute(self, sql, params=None):
        self.cursor.execute(sql, params or ())
    
    def query(self, sql, params=None):
        self.cursor.execute(sql, params or ())

        return self.fetchall()

class Especialidade(Connection):

    def __init__(self):
        Connection.__init__(self)

    def insert(self, *args):
        try:
            sql = "INSERT INTO tb_especialidades (especialidade, link) VALUES (%s, %s)"
            self.execute(sql, args)
            self.commit()
        except Exception as e:
            print('Insertion error. ', e)

    def select(self):
        sql = "SELECT * FROM tb_especialidades"
        row = self.query(sql)

        return row
    
    def get_all(self):
        rows = self.select()

        specialties = []
        
        for specialty in rows:
            specialties.append({'id': specialty[0], 'name': specialty[1], 'link': specialty[2]})

        return specialties

    
