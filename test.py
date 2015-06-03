#!/usr/bin/python

import os
import unittest
from subprocess import check_output
import SetUp


class TestOwnerModification(unittest.TestCase):

    #Saving current file owner
    server_file_path = os.getcwd()+'/'+SetUp.dirslist[0]+'/'+SetUp.filenames[0]
    client_file_path = os.getcwd()+'/'+SetUp.dirslist[1]+'/'+SetUp.filenames[0]
    d_file_info = check_output(['ls', '-l', server_file_path])
    d_owner = d_file_info.split(" ")[2]

    def setUp(self):
        SetUp.logger.info("SetUp")
        #Changing owner
        SetUp.changeOwner(SetUp.usernames[0], self.server_file_path)
        file_info = check_output(['ls', '-l', self.client_file_path])
        owner = file_info.split(" ")[2]
        SetUp.logger.info(owner+" "+SetUp.usernames[0])

    def tearDown(self):
        #SetUp.logger.info("tearDown")
        #SetUp.changeOwner(self.d_owner, self.file_path)
        pass

    def testPositiveResult(self):
        #SetUp.logger.info("Assertion")
        #file_info = check_output(['ls', '-l', self.file_path])
        #owner = file_info.split(" ")[2]
        #SetUp.logger.info(owner+" "+SetUp.usernames[0])
        #self.assertEqual(owner, SetUp.usernames[0], "Message")
        pass

if __name__ == '__main__':
    unittest.main()
