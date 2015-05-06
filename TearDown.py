#!/usr/bin/python

import logging
from subprocess import call, check_output
import shutil
import os

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
def unmountShare():
    """Unmounting shared directory"""
    logger.info("Trying to unmount shared directory")
    call(["umount","-l",str(os.getcwd())+"/clienttestdir"])
    logger.info("Directory has been successfuly unmounted")

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

@handleError
def uninstallPackages():
    """Uninstalling packages"""
    logger.info("Trying to uninstall packages")
    call(["apt-get","-y","--purge","remove","nfs-kernel-server","nfs-common"])

@handleError
def deleteDirs():
    """Deleting dirs"""
    logger.info("Trying to delete test dirs and files")
    dirslist = ['servertestdir','clienttestdir']
    for dirname in dirslist:
        try:
            shutil.rmtree(dirname)
        except OSError, e:
            logger.warning("File is missing: "+str(e))
		

unmountShare()
deleteExports()
deleteDirs()
uninstallPackages()
