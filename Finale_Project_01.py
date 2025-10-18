import maya.cmds as cmds
import random

def my_window():
    if cmds.window("ctc", exists=True):
        cmds.deleteUI("ctc")
        
    cmds.window("ctc", title="Click The Cube", widthHeight=(300, 400), backgroundColor=(0.1, 0.2, 0.3))
    cmds.columnLayout(adjustableColumn=True, columnAlign="center")
    cmds.text(label="Click The Cube", height=(100), backgroundColor=(0.0, 0.1, 0.2))
    
    cmds.radioCollection("Gamemode")
    cmds.radioButton(label=" 😪 Endless")
    cmds.radioButton(label=" 😌 Normal", select=True)
    cmds.radioButton(label=" 💀 Hardcore")
    
    cmds.rowColumnLayout(numberOfColumns=2, columnWidth=[(1, 150), (2, 150)])
    cmds.button(label="😀 Start", backgroundColor=(0, 0, 0), command=lambda x: my_timer())
    cmds.button(label="😡 Close", backgroundColor=(0, 0, 0), command=close_Mainwindow)
    cmds.showWindow("ctc")
    
def close_Mainwindow(*args):
    if cmds.window("ctc", exists=True):
        cmds.deleteUI("ctc")
    
my_window()