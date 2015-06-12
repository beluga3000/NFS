#!/usr/bin/python

import os
import unittest
import Common
import SetUp

class TestFileContentModificationWithPermission(unittest.TestCase):

    def setUp(self):
        # Set a test line to write
        self.testline = "This is a test line"
        #Save file path
        self.file_path_server = os.getcwd()+'/'+SetUp.dirslist[0]+'/'+SetUp.filenames[0]
        self.file_path_client = os.getcwd()+'/'+SetUp.dirslist[1]+'/'+SetUp.filenames[0]
        # Save default file permissions
        self.d_permission = Common.getPermissions(self.file_path_server)
        # Set permission to write
        self.permissions_to_set = "777"
        Common.setPermission(self.permissions_to_set, self.file_path_server)
        # Save default file content
        self.d_file_content = Common.getFileContent(self.file_path_server)
        SetUp.logger.info(self.d_file_content)

    def tearDown(self):
        # Restore default file content
        Common.writeToFile(self.d_file_content, self.file_path_server)
        # Restore default file permissions
        Common.setPermission(self.d_permission, self.file_path_server)

    def testWriteToFile(self):
        # Write a line to file
        Common.writeToFile(self.testline, self.file_path_server)
        SetUp.logger.info(Common.getFileContent(self.file_path_client))
        # Assert client file changes
        self.assertIn(self.testline, Common.getFileContent(self.file_path_client))


if __name__ == "__main__":
    unittest.main()