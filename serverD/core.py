import os
from serverD.settings import load_config
from serverD.serverManager import serverManager


SERVER_BASE_DATA = {

    "put": "{type} {user} {host} {pwd} {port} {localPath} {serverPath}",
    "get": "{type} {user} {host} {pwd} {port} {localPath} {serverPath}",
    "login": "{type} {user} {host} {pwd} {port}",
    # "login_pem": "{user} {host} {pem_path} {port}",

}


class serverDcore(object):
    def __init__(self):
        super(serverDcore, self).__init__()
        self.conf = load_config("cli")
        self.scripts_folder = os.path.join(os.path.dirname(os.path.abspath(__file__)), "scripts")
        self.manager = serverManager()

    def runCommand(self, command_type, **kwargs):
        command_data = SERVER_BASE_DATA.get(command_type).format(**kwargs)
        script_path = os.path.join(self.scripts_folder, self.conf['scripts'][command_type])
        cmd = script_path + " " + command_data
        os.system(cmd)

    def addServer(self, server_name, host, port, user, passwd=None, pem_path=None):
        if not passwd and not pem_path:
            print("passwd and pem both None")
            return False
        self.manager.addServer(server_name, host, port, user, passwd, pem_path)
        return True

    def deleteServer(self, server_name):
        self.manager.deleteServer(server_name)

    def login(self, server_name):
        host, port, user, passwd, pem_path = self.manager.getServer(server_name)
        type, pwd = ('pwd', passwd) if not pem_path else ("key", pem_path)
        self.runCommand('login', type=type, host=host, port=port, user=user, pwd=pwd)

    def get(self, server_name, serverPath, localPath):
        host, port, user, passwd, pem_path = self.manager.getServer(server_name)
        type, pwd = ('pwd', passwd) if not pem_path else ("key", pem_path)
        self.runCommand("get", type=type, host=host, port=port, user=user, pwd=pwd, localPath=localPath, serverPath=serverPath)

    def put(self, server_name, localPath, serverPath):
        host, port, user, passwd, pem_path = self.manager.getServer(server_name)
        type, pwd = ('pwd', passwd) if not pem_path else ("key", pem_path)
        self.runCommand("put", type=type, host=host, port=port, user=user, pwd=pwd, localPath=localPath, serverPath=serverPath)
