import sqlite3
import os


from settings import DB_PATH

class DBManager:
    def __init__(self,db_path: str) -> None:
        self.db_path = db_path

    def check_base(self):
        return os.path.exists(self.db_path)

    def connect_to_base(self):
        conn = sqlite3.connect(self.db_path)
        cur = conn.cursor()
        return conn,cur

    def create_base(self, SCRIPTS_TABLES_PATH: str,SCRIPTS_RIMARY_DATA_PATH: str):
        conn, cur = self.check_base()
        try:
            cur.executescript(open(SCRIPTS_TABLES_PATH).read())
            cur.executescript(open(SCRIPTS_RIMARY_DATA_PATH).read())
            conn.commit()
            conn.close()
        except sqlite3.Error as ex:
            print(ex)
            os.remove(self,DB_PATH)


    def execute(self, query: str, args=(), many: bool = True):
        conn, cur = self.connect_to_base()
        try:
            res = cur.execute(query, args)
            result = res.fetchall() if many else res.fetchone()
            conn.commit()
            return {"code": 200, "data": result}
        except sqlite3.Error as er:
            print(str(er))
            return {"code": 500}
        finally:
                conn.close()


base_manager = DBManager(DB_PATH)