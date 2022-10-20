import maya.cmds as cmds

def incrementFile():
    fileName = maya.cmds.file(sceneName=True, shortName=True, query=True)
    asset, task, artist, version, ext = fileName.split(".")
    
    currentVersion = int(version)
    newVersion = str(currentVesion + 1)
    
    newFile = ".".join([asset, task, artist, version, ext])
    maya.cmds.file(rename=newFile)
    print(f"Saving to: \'{maya.cmds.file(save=True, type='mayaAscii')}\'")