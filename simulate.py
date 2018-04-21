import pymouse

mouse = pymouse.PyMouse()


def Coord():
    return mouse.screen_size()


def mousemove(posx,posy):
    mouse.move(int(posx), int(posy))
    print(posx,posy)


def mousedown(posx,posy):
    print(posx, posy)
    mouse.move(int(posx), int(posy))
    # mouse.press(int(posx), int(posy), button=1)


def mouseup(posx,posy):
    print(posx, posy)
    mouse.move(int(posx), int(posy))
    # mouse.release(int(posx), int(posy), 1)