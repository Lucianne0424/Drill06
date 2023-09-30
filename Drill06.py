from pico2d import *
import random

Width, Height = 1280, 960
open_canvas(Width, Height)

handImg = load_image('hand_arrow.png')
backGroundImg = load_image('TUK_GROUND.png')
boy = load_image('animation_sheet.png')

loop = True

dir = True
frame = 0

List = [[Width // 2, Height //2]]
x,y = List[0][0],  List[0][1]

listCount = 1
moveCount = 0



def mouse_event():
    events = get_events()

    for event in events:
        if event.type == SDL_QUIT:
            loop = False
        elif event.type == SDL_MOUSEBUTTONDOWN:
            nextLocation(event.x, Height - 1 - event.y)


def nextLocation(x, y):
    global List, listCount

    List += [[x, y]]
    listCount += 1


def PaintImg(dir):
    global frame
    mouse_event()
    clear_canvas()
    backGroundImg.draw(Width // 2, Height // 2)

    for i in range(moveCount + 1, listCount):
        handImg.draw(List[i][0], List[i][1])
    if dir:
        boy.clip_draw(frame * 100, 0, 100, 100, x, y)
    else:
        boy.clip_draw(frame * 100, 100, 100, 100, x, y)

    update_canvas()
    frame = (frame + 1) % 8
    delay(0.1)

def moveBoy():
    global frame, x, y, dir, moveCount

    if listCount != moveCount + 1:
        for i in range(0, 100 + 1, 3):
            t = i / 100
            x = (1 - t) * List[moveCount][0] + t * List[moveCount + 1][0]
            y = (1 - t) * List[moveCount][1] + t * List[moveCount + 1][1]

            if List[moveCount][0] > List[moveCount + 1][0]:
                dir = True
            else:
                dir = False
            PaintImg(dir)

        moveCount += 1






while loop:
    mouse_event()
    PaintImg(dir)
    moveBoy()