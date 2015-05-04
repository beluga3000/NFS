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
def mountShare():
    """Mounting share directory"""
    logger.info("Trying to start nfs-kernel-server")
    call(["/etc/init.d/nfs-kernel-server","start"])
    logger.info("Trying to mount share directory")
    call(["mount","127.0.0.1:"+str(os.getcwd())+"/servertestdir",str(os.getcwd())+"/clienttestdir"])
    logger.info("Directory has been successfuly mounted")

mountShare()
