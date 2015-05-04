#!/usr/bin/python

import os
import logging
from subprocess import call, check_output
import pexpect

#Logging description
logger = logging.getLogger()
logger.setLevel(logging.DEBUG)
formatter = logging.Formatter("%(asctime)s:%(msecs).03d:%(levelname)s: %(message)s", "%d/%m/%Y %I/%M/%S")
ch = logging.StreamHandler()
ch.setLevel(logging.DEBUG)
ch.setFormatter(formatter)
logger.addHandler(ch)
logger.info("Logging has been activated")

#Exception handler
def handleError(function):
    def handleProblems():
        try:
            function()
        except Exception,e:
            logger.error("There was an error during installation process: "+str(e))
        else:
            logger.info(function.__doc__+" done")
    return handleProblems

@handleError
def deleteExports():
    """Returning exports list to deafault state"""
    logger.info("Trying to return export list to default state")
    with open('/etc/exports','r+') as f:
        d = f.readlines()
        f.seek(0)
        for i in d:
            if 'servertestdir' not in i:
                f.write(i)
        f.truncate()
    logger.info("Exports file has been changed")

deleteExports()
