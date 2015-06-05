#!/usr/bin/python

import os
import unittest
import Common
import SetUp

class TestGroupModification(unittest.TestCase):
    def setUp(self):
        SetUp.logger.info('Saving default group name')
        self.file_path = os.getcwd()+'/'+SetUp.dirslist[0]+'/'+SetUp.filenames[0]
        self.d_group = Common.getGroup(self.file_path)

    def tearDown(self):
        SetUp.logger.info('Restoring default group name')
        Common.changeGroup(self.d_group, self.file_path)
        SetUp.logger.info('Current group: %s, default group: %s' % (Common.getGroup(self.file_path), self.d_group))

    def testGroupChanging(self):
        """Changing file group"""
        Common.changeGroup(SetUp.groupnames[0], self.file_path)
        owner = Common.getGroup(self.file_path)
        SetUp.logger.info('Current group: %s, default group: %s' % (owner, self.d_group))
        self.assertEqual(SetUp.groupnames[0], owner, self.testGroupChanging.__doc__ + ' FAILED')
        SetUp.logger.info(self.testGroupChanging.__doc__+' has been finished')


if __name__ == "__main__":
    unittest.main()