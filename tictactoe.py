from turtle import *

from freegames import line

def grid():
    """Draw tic-tac-toe grid."""
    line(-67, 200, -67, -200)
    line(67, 200, 67, -200)
    line(-200, -67, 200, -67)
    line(-200, 67, 200, 67)

def drawx(x, y):
    """Draw X player."""
    color('blue')  # Define a cor para X
    width(3)  # Define a largura da linha para X
    up()
    goto(x + 10, y + 10)
    down()
    goto(x + 123, y + 123)
    up()
    goto(x + 10, y + 123)
    down()
    goto(x + 123, y + 10)

def drawo(x, y):
    """Draw O player."""
    color('red')  # Define a cor para O
    width(3)  # Define a largura da linha para O
    up()
    goto(x + 67, y + 5)
    down()
    circle(62)

def floor(value):
    """Round value down to grid with square size 133."""
    return ((value + 200) // 133) * 133 - 200

state = {'player': 0}
players = [drawx, drawo]

def tap(x, y):
    """Draw X or O in tapped square."""
    x = floor(x)
    y = floor(y)
    player = state['player']
    draw = players[player]
    draw(x, y)
    update()
    state['player'] = not player

setup(420, 420, 370, 0)
hideturtle()
tracer(False)
grid()
update()
onscreenclick(tap)
done()
