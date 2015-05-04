#!/usr/bin/python

import logging
from subprocess import call, check_output
import shutil

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
        except Exception, e:
            logger.error("There was an error during installation process: "+str(e))
        else:
            logger.info(function.__doc__ +" done")
    return handleProblems

#Creating testing dirs and files

@handleError
def installPackages():
    """Installing packages"""
    logger.info("Trying to install packages")
    call(["apt-get","install","nfs-kernel-server","nfs-common"])

installPackages()

