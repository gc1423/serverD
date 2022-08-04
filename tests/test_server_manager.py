# -*- coding: utf-8 -*-
import os.path
import unittest
from serverD.serverManager import serverManager


class serverManagerTest(unittest.TestCase):
    """Advanced test cases."""

    def test_db(self):
        server = serverManager()
        self.assertTrue(os.path.exists(server.db_path))

    def test_server_manage(self):
        server = serverManager()
        server_name = "test_server"
        data = ("127.0.0.1", 22, 'work', "1234")
        server.addServer(server_name, "127.0.0.1", 22, 'work', "1234")
        self.assertEqual(data, server.getServer(server_name))


if __name__ == '__main__':
    unittest.main()
