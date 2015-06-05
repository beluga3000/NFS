#!/usr/bin/python

import os
import unittest
import Common
import SetUp

class TestOwnerModification(unittest.TestCase):

    def setUp(self):
        self.permissions_to_set = "000"
        SetUp.logger.info('Saving default file permissions')
        self.file_path = os.getcwd()+'/'+SetUp.dirslist[0]+'/'+SetUp.filenames[0]
        self.d_permissions = Common.getPermissions(self.file_path)

    def tearDown(self):
        SetUp.logger.info('Restoring file permissions')
        Common.setPermission(self.d_permissions, self.file_path)
        SetUp.logger.info('Current permissions: %s, default permissions: %s' % (Common.getPermissions(self.file_path), self.d_permissions))

    def testPermissionsChanging(self):
        """Changing file permissions"""
        Common.setPermission(self.permissions_to_set, self.file_path)
        current_permissions = Common.getPermissions(self.file_path)
        SetUp.logger.info('Current permissions: %s, default permissions: %s, permissions to set: %s' % (current_permissions, self.d_permissions, self.permissions_to_set))
        self.assertEqual(self.permissions_to_set, current_permissions, self.testPermissionsChanging.__doc__ + ' FAILED')
        SetUp.logger.info(self.testPermissionsChanging.__doc__+' has been finished')


if __name__ == "__main__":
    unittest.main()