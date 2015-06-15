#!/usr/bin/python

import os
import unittest
import Common
import SetUp

class TestOwnerModification(unittest.TestCase):

    def setUp(self):
        SetUp.logger.info('Saving default owner name')
        self.file_path_server = os.getcwd()+'/'+SetUp.dirslist[0]+'/'+SetUp.filenames[0]
        self.file_path_client = os.getcwd()+'/'+SetUp.dirslist[1]+'/'+SetUp.filenames[0]
        self.d_owner = Common.getOwner(self.file_path_server)

    def tearDown(self):
        SetUp.logger.info('Restoring default owner name')
        Common.changeOwner(self.d_owner, self.file_path_server)
        SetUp.logger.info('Current owner: %s, default owner: %s' % (Common.getOwner(self.file_path_client), self.d_owner))

    def testOwnerChanging(self):
        """Changing file owner"""
        Common.changeOwner(SetUp.usernames[0], self.file_path_server)
        owner = Common.getOwner(self.file_path_client)
        SetUp.logger.info('Current owner: %s, default owner: %s' % (owner, self.d_owner))
        self.assertEqual(SetUp.usernames[0], owner, self.testOwnerChanging.__doc__ + ' FAILED')
        SetUp.logger.info(self.testOwnerChanging.__doc__+' has been finished')


if __name__ == "__main__":
    unittest.main()