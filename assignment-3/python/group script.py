import os
os.environ["asset"] = "empty group"

import maya.cmds as cmds
cmds.group( em=True, name=os.environ["asset"])
