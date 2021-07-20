from ursina import *

def update():
    if held_keys['a']:
        test.x -= 4 * time.dt

app = Ursina()

test = Entity(model = 'quad', color = color.red, scale = (1,4), position = (5,1) )

app.run()
