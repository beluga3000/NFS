from subprocess import call, PIPE, check_output
from SetUp import logger
import re

def changeOwner(owner, filename):
    """Changing file owner name"""
    try:
        call(['chown', owner, filename], stderr=PIPE)
    except Exception, e:
        logger.error("There was an error: "+str(e))
    else:
        logger.info((changeOwner.__doc__ +" has finished OK"))

def changeGroup(group, filename):
    """Changing file group name"""
    try:
        call(['chgrp', group, filename], stderr=PIPE)
    except Exception, e:
        logger.error("There was an error: "+str(e))
    else:
        logger.info((changeGroup.__doc__ +" has finished OK"))

def getOwner(file_path):
    return check_output(['ls', '-l', file_path]).split(' ')[2]

def getGroup(file_path):
    return check_output(['ls', '-l', file_path]).split(' ')[3]

def setPermission(permission, file_path):
    """Changing file permissions"""
    try:
        call(['chmod', permission, file_path], stderr=PIPE)
    except Exception, e:
        logger.error("There was an error: "+str(e))
    else:
        logger.info((setPermission.__doc__ +" has finished OK"))

def getPermissions(file_path):
    """Getting file permissions"""
    file_info = re.search('(?<=Access: \(0)(\d{3})', check_output(['stat', file_path]))
    return file_info.group(0)