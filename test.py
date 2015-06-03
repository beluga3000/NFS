import unittest
from subprocess import check_output
from SetUp import logger, usernames


class TestOwnerModification(unittest.TestCase):

    def setUp(self):
        logger.info("SetUp")


    def tearDown(self):
        logger.info("tearDown after test")


    def testPositiveResult(self):
        logger.info("Check if testuser was created")
        self.assertEqual(int(check_output(['id', '-u', usernames[0]])), 1002)
        self.assertEqual(int(check_output(['id', '-u', usernames[1]])), 1003)

if __name__ == '__main__':
    unittest.main()
