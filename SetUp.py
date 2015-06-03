#!/usr/bin/python

import os
import logging
from subprocess import call, PIPE

#Creating custom logging handler
import crypt

dirslist = ['servertestdir','clienttestdir']
filenames = ['testfile1', 'testfile2']
usernames = ['testuser1', 'testuser2']
groupnames = ['testgroup1', 'testgroup2']

class MyHandler(logging.StreamHandler):
    def __init__(self):
        logging.StreamHandler.__init__(self)
        fmt = "%(asctime)s:%(msecs).03d:%(levelname)s: %(message)s"
        fmt_date = "%d/%m/%Y %I/%M/%S"
        formatter = logging.Formatter(fmt, fmt_date)
        self.setFormatter(formatter)

#Logging description
logger = logging.getLogger("setup")
logger.setLevel(logging.DEBUG)
logger.addHandler(MyHandler())
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

#Creating test dirs
@handleError
def createDirs():
    """Creating testdirs"""
    logger.info("Trying to create test dirs")
    for dirname in dirslist:
        try:
            os.makedirs(dirname)
        except Exception, e:
            logger.error("There was an error during installation process: "+str(e))

#Creating test files
@handleError
def createFiles():
    """Creating test files"""
    os.chdir(os.getcwd()+'/servertestdir')
    open(filenames[0], 'a').close()
    open(filenames[1], 'a').close()
    os.chdir('..')

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
    call(["exportfs","-a"])
    logger.info("Trying to mount share directory")
    call(["mount","-o","bg,intr,hard","127.0.0.1:"+str(os.getcwd())+"/servertestdir",str(os.getcwd())+"/clienttestdir"])
    logger.info("Directory has been successfuly mounted")

def createUser(username):
    """Creating new user"""
    try:
        call(["useradd", username], stderr=PIPE)
    except Exception, e:
        logger.error("There was an error during installation process: "+str(e))
    else:
        logger.info((createUser.__doc__ +" done"))

def createGroup(groupname):
    """Creating new group"""
    try:
        call(['groupadd', groupname], stderr=PIPE)
    except Exception, e:
        logger.error("There was an error during installation process: "+str(e))
    else:
        logger.info((createGroup.__doc__ +" done"))

def attachUser(username, groupname):
    """Creating new group"""
    try:
        call(['adduser', username, groupname], stderr=PIPE)
    except Exception, e:
        logger.error("There was an error during installation process: "+str(e))
    else:
        logger.info((attachUser.__doc__ +" done"))

def changeOwner(owner, filename):
    """Changing owner"""
    try:
        call(['chown', owner, filename], stderr=PIPE)
    except Exception, e:
        logger.error("There was an error during installation process: "+str(e))
    else:
        logger.info((changeOwner.__doc__ +" done"))

def changeGroup(group, filename):
    """Changing group"""
    try:
        call(['chgrp', group, filename], stderr=PIPE)
    except Exception, e:
        logger.error("There was an error during installation process: "+str(e))
    else:
        logger.info((changeGroup.__doc__ +" done"))

if __name__=="__main__":
    createDirs()
    createFiles()
    fillExports()
    mountShare()
    createUser(usernames[0])
    createUser(usernames[1])
    createGroup(groupnames[0])
    createGroup(groupnames[1])
    attachUser(usernames[0], groupnames[0])
    attachUser(usernames[1], groupnames[1])