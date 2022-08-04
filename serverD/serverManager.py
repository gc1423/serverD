import os
import sys
import sqlite3
from serverD.settings import load_config
from serverD.exceptions import ServerNotFound, ServerAlreadyExist


class serverManager(object):
    def __init__(self):
        super(serverManager, self).__init__()
        self.conf = load_config("cli")
        self.db_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), self.conf['database']['db_name'])
        self.connection = sqlite3.connect(self.db_path)
        self.cursor = self.connection.cursor()
        self.initDB()

    def initDB(self):
        self.cursor.execute(self.conf['database']['init_sql'])

    def addServer(self, server_name, host, port, user, passwd, pem_path):
        data = [(server_name, host, user, port, passwd, pem_path)]
        sql = f"""insert into {self.conf['database']['server_table']} VALUES(?, ?, ?, ?, ?, ?)"""
        self.cursor.executemany(sql, data)
        self.connection.commit()
        return self.cursor.fetchone()

    def deleteServer(self, server_name):
        sql = f"""delete from {self.conf["database"]["server_table"]} where serverName = "{server_name}" """
        self.cursor.execute(sql)
        self.connection.commit()
        return self.cursor.fetchone()

    def getServer(self, server_name):
        if not isinstance(server_name, str):
            server_name = "{}".format(server_name)
        sql = f"""select host, port, user, pwd, pem_path from {self.conf['database']['server_table']} where serverName = '{server_name}'"""
        login_tuple = self.cursor.execute(sql).fetchone()
        if not login_tuple:
            raise ServerNotFound("%s server not found" % server_name)
        return login_tuple
