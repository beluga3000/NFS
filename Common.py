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

def setPermissionByReference(file1_path, file2_path):
    """Changing file permissions by reference"""
    try:
        call(['chmod', '--reference', file1_path, file2_path], stderr=PIPE)
    except Exception, e:
        logger.error("There was an error: "+str(e))
    else:
        logger.info((setPermissionByReference.__doc__ +" has finished OK"))

def getPermissions(file_path):
    """Getting file permissions"""
    file_info = re.search('(?<=Access: \(0)(\d{3})', check_output(['stat', file_path]))
    return file_info.group(0)

def getFileContent(file_path):
    """Getting file content"""
    logger.info("Trying to get file content")
    with open(file_path,'r+') as f:
        d = f.read()
        logger.info((getFileContent.__doc__ +" has finished OK"))
        return d

def writeToFile(content, file_path):
    """Writing to file"""
    logger.info("Trying to write file content")
    with open(file_path,'w+') as f:
        f.write(content)
        logger.info((writeToFile.__doc__ +" has finished OK"))
