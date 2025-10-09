import maya.cmds as cmds
import random

def my_window():
    if cmds.window("ctc", exists=True):
        cmds.deleteUI("ctc")
        
    cmds.window("ctc", title="Click The Cube", widthHeight=(300, 400), sizeable=False)
    cmds.columnLayout(adjustableColumn=True, columnAlign="center")
    
    cmds.radioCollection("Gamemode")
    cmds.radioButton(label=" 😪 Endless")
    cmds.radioButton(label=" 😌 Normal", select=True)
    cmds.radioButton(label=" 💀 Hardcore")
    
    cmds.rowColumnLayout(numberOfColumns=2, columnWidth=[(1, 150), (2, 150)])
    cmds.button(label="😀 Start", command=lambda x: my_timer())
    cmds.button(label="😡 Close", command=close_Mainwindow)
    cmds.showWindow("ctc")
    
def close_Mainwindow(*args):
    if cmds.window("ctc", exists=True):
        cmds.deleteUI("ctc")
    
my_window()