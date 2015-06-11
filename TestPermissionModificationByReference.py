#!/usr/bin/python

import os
import unittest
import Common
import SetUp

class TestDirectPermissionModificationByReference(unittest.TestCase):

    def setUp(self):
        self.permissions_to_set = "777"
        SetUp.logger.info('Saving default file permissions')
        self.file1_path = os.getcwd()+'/'+SetUp.dirslist[0]+'/'+SetUp.filenames[0]
        self.file2_path = os.getcwd()+'/'+SetUp.dirslist[0]+'/'+SetUp.filenames[1]
        self.d1_permissions = Common.getPermissions(self.file1_path)
        self.d2_permissions = Common.getPermissions(self.file2_path)
        SetUp.logger.info("Default permission values are: %s and %s" % (Common.getPermissions(self.file1_path), Common.getPermissions(self.file2_path)))
        Common.setPermission(self.permissions_to_set, self.file1_path)
        SetUp.logger.info("File 1 permissions = %s, file 2 permissions = %s" % (Common.getPermissions(self.file1_path), Common.getPermissions(self.file2_path)))

    def tearDown(self):
        SetUp.logger.info('Restoring file permissions')
        Common.setPermission(self.d1_permissions, self.file1_path)
        Common.setPermission(self.d2_permissions, self.file2_path)
        SetUp.logger.info("File 1 permissions = %s, file 2 permissions = %s" % (Common.getPermissions(self.file1_path), Common.getPermissions(self.file2_path)))

    def testPermissionsChangingByReference(self):
        """Changing file permissions"""
        Common.setPermissionByReference(self.file1_path, self.file2_path)
        SetUp.logger.info("File 1 permissions = %s, file 2 permissions = %s" % (Common.getPermissions(self.file1_path), Common.getPermissions(self.file2_path)))
        self.assertEqual(Common.getPermissions(self.file1_path), Common.getPermissions(self.file2_path))


if __name__ == "__main__":
    unittest.main()