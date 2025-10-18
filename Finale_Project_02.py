import maya.cmds as cmds
import random
import threading
import time

s = 0     
t = 30  
score_text = None
timer_text = None
c1 = None  
game_running = True  

def my_timer():
    global score_text, timer_text, c1, s, t, game_running
    s = 0
    t = 30
    game_running = True

    if cmds.window("ctc", exists=True):
        cmds.deleteUI("ctc")
    if cmds.window("timer", exists=True):
        cmds.deleteUI("timer")

    win = cmds.window("timer", title="Click the Cube", widthHeight=(400, 400))
    form = cmds.formLayout()

    info = cmds.columnLayout(adjustableColumn=True, columnAlign="center")
    cmds.rowColumnLayout(numberOfColumns=2,
                         columnWidth=[(1, 100), (2, 100)],
                         columnAlign=[(1, "right"), (2, "left")])
    cmds.text(label="Score : ")
    score_text = cmds.text(label=str(s))
    cmds.text(label="Timer : ")
    timer_text = cmds.text(label=str(t))
    cmds.setParent("..")
    cmds.setParent("..")

    c1 = cmds.button(label="", width=50, height=50,
                     backgroundColor=(0, 1, 0), command=count_scores)

    stop = cmds.button(label="😡 Stop", width=100, height=40, backgroundColor=(0, 0, 0), command=lambda x: my_score())

    cmds.formLayout(form, edit=True,
        attachForm=[(info, 'top', 10),(info, 'left', 100),(info, 'right', 100),
            (stop, 'left', 150),(stop, 'bottom', 10)],
        attachPosition=[(c1, 'left', 0, 50), (c1, 'top', 0, 30)])

    cmds.showWindow(win)
    click_scores(form, c1)

    threading.Thread(target=update_timer, daemon=True).start()


def update_timer():
    global t, timer_text, game_running
    while t > 0 and game_running:
        time.sleep(1)
        t -= 1
        if timer_text:
            cmds.evalDeferred(lambda: cmds.text(timer_text, edit=True, label=str(t)))
    
    if game_running:
        cmds.evalDeferred(lambda: my_score())  


def count_scores(*args):
    global s, t, score_text, timer_text, c1, game_running
    if not game_running:
        return

    s += 1
    t += 1  
    cmds.text(score_text, edit=True, label=str(s))
    cmds.text(timer_text, edit=True, label=str(t))  

    parent_form = cmds.button(c1, query=True, parent=True)
    click_scores(parent_form, c1)



def click_scores(form_layout, button):
    rand_x = random.randint(0, 90)
    rand_y = random.randint(10, 90) 

    cmds.formLayout(form_layout, edit=True,
        attachPosition=[(button, 'left', 0, rand_x),(button, 'top', 0, rand_y)])



my_timer()
