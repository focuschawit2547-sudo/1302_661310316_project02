import maya.cmds as cmds
import random

s = 0     
t = 10 #ไม่ได้ใช้
score_text = None
c1 = None  


def my_timer():
    global score_text, c1, s, t
    s = 0
    t = 10
    
    if cmds.window("ctc", exists=True):
        cmds.deleteUI("ctc")
    if cmds.window("timer", exists=True):
        cmds.deleteUI("timer")

    win = cmds.window("timer", title="Click the Cube", widthHeight=(400, 400), sizeable=False)
    form = cmds.formLayout()

    info = cmds.columnLayout(adjustableColumn=True, columnAlign="center")
    cmds.rowColumnLayout(numberOfColumns=2,
                         columnWidth=[(1, 100), (2, 100)],
                         columnAlign=[(1, "right"), (2, "left")])
    cmds.text(label="Score : ")
    score_text = cmds.text(label=str(s))
    cmds.text(label="Timer : ")
    cmds.text(label=str(t))
    cmds.setParent("..")
    cmds.setParent("..")

    c1 = cmds.button(label="", width=50, height=50,
                     backgroundColor=(0, 1, 0), command=count_scores)

    stop = cmds.button(label="😡 Stop", width=100, height=40, command=lambda x: my_score())


    cmds.formLayout(form, edit=True,
        attachForm=[(info, 'top', 10),(info, 'left', 100),(info, 'right', 100),
            (stop, 'left', 150),(stop, 'bottom', 10)],
        attachPosition=[(c1, 'left', 0, 50), (c1, 'top', 0, 30)])

    cmds.showWindow(win)
    click_scores(form, c1)


def count_scores(*args):

    global s, score_text, c1
    s += 1
    cmds.text(score_text, edit=True, label=str(s))

    parent_form = cmds.button(c1, query=True, parent=True)
    click_scores(parent_form, c1)


def click_scores(form_layout, button):

    rand_x = random.randint(0, 90)
    rand_y = random.randint(40, 75) 

    cmds.formLayout(form_layout, edit=True,
        attachPosition=[(button, 'left', 0, rand_x),(button, 'top', 0, rand_y)])


my_timer()

