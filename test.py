#!/usr/bin/python

import os
import unittest
from subprocess import check_output
import SetUp


class TestOwnerModification(unittest.TestCase):

    #Saving current file owner
    def __init__(self, *args, **kwargs):
        self.server_file_path = os.getcwd()+'/'+SetUp.dirslist[0]+'/'+SetUp.filenames[0]
        self.client_file_path = os.getcwd()+'/'+SetUp.dirslist[1]+'/'+SetUp.filenames[0]
        self.d_file_info = check_output(['ls', '-l', self.server_file_path])
        self.d_owner = self.d_file_info.split(" ")[2]
        SetUp.logger.info(self.d_owner)
        super(TestOwnerModification, self).__init__(*args, **kwargs)

    def setUp(self):
        SetUp.logger.info("SetUp")
        #Changing owner
        SetUp.changeOwner(SetUp.usernames[0], self.server_file_path)
        file_info = check_output(['ls', '-l', self.client_file_path])
        self.owner = file_info.split(" ")[2]
        SetUp.logger.info(self.owner+" "+SetUp.usernames[0])

    def test_Name_changed_back(self):
        SetUp.logger.info("Assertion")
        SetUp.logger.info(self.d_owner)
        SetUp.logger.info(check_output(['ls', '-l', self.client_file_path]).split(" ")[2])
        self.assertEqual(SetUp.usernames[0], check_output(['ls', '-l', self.client_file_path]).split(" ")[2], "FAAAAAIL")

    def tearDown(self):
        SetUp.logger.info("tearDown with default owner %s" %self.d_owner)
        SetUp.changeOwner(self.d_owner, self.server_file_path)
        owner = check_output(['ls', '-l', self.server_file_path]).split(" ")[2]
        SetUp.logger.info(owner+" "+SetUp.usernames[0])

if __name__ == '__main__':
    unittest.main()
