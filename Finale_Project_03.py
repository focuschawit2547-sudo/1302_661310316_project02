def my_score(*args):
    if cmds.window("timer", exists=True):
        cmds.deleteUI("timer")

    if cmds.window("score", exists=True):
        cmds.deleteUI("score")

    cmds.window("score", title="GAME OVER", widthHeight=(300, 350), sizeable=False)
    
    cmds.columnLayout(adjustableColumn=True, columnAlign="center")
    cmds.text(label="GAME OVER")
    
    cmds.separator(height=10, style='none')  
    
    cmds.rowColumnLayout(numberOfColumns=2, columnWidth=[(1, 200), (2, 50)])
    cmds.text(label="Scores : ")
    cmds.text(label=str(s))
    cmds.setParent("..") 

    cmds.separator(height=10, style='none')  

    cmds.columnLayout(adjustableColumn=True, columnAlign="center")
    cmds.button(label="😐 Ok", width=100, command=close_window)

    cmds.showWindow("score")


def close_window(*args):
    my_window()
    s = 0  # Score
    t = 0
    if cmds.window("score", exists=True):
        cmds.deleteUI("score")


my_score()