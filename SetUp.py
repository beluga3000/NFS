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
        except Exception, e:
            logger.error("There was an error during installation process: "+str(e))
        else:
            logger.info(function.__doc__ +" done")
    return handleProblems

#Creating testing dirs and files
@handleError
def createDirs():
    """Creating testdirs"""
    logger.info("Trying to create test dirs and files")
    os.makedirs('servertestdir')
    os.makedirs('clienttestdir')
    os.chdir(os.getcwd()+'/servertestdir')
    open('testfile1', 'a').close()
    open('testfile2', 'a').close()
    os.chdir('..')

@handleError
def installPackages():
    """Installing packages"""
    logger.info("Trying to install packages")
    call(["apt-get","install","nfs-kernel-server","nfs-common"])

@handleError
def fillExports():
    """Filling exports list"""
    logger.info("Trying to fill export list")
    with open("/etc/exports", "a") as exports:
        exports.write("\n"+str(os.getcwd())+'/servertestdir'+' 127.0.0.1(rw,async)')
        logger.info("Exports file has been changed")

@handleError
def mountShare():
    """Mounting share directory"""
    logger.info("Trying to start nfs-kernel-server")
    call(["/etc/init.d/nfs-kernel-server","start"])
    logger.info("Trying to mount share directory")
    call(["mount","127.0.0.1:"+str(os.getcwd())+"/servertestdir",str(os.getcwd())+"/clienttestdir"])
    logger.info("Directory has been successfuly mounted")

createDirs()
installPackages()
fillExports()
mountShare()
