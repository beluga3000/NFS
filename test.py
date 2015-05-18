import unittest
import os
import sys
from SetUp import logger, createUser, deleteUser

#Multiplication tests set
class TestOwnerModification(unittest.TestCase):

    def setUp(self):
        logger.info("SetUp")
        createUser("testusername")

    def tearDown(self):
        logger.info("tearDown after test")
        deleteUser("testusername")

    def testPositiveResult(self):
        logger.info("Check if testuser was created")
        self.assertEqual(num1*num2, test_result)

