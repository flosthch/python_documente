from tkinter import *
import tkinter.font as tkFont
from random import randint
HEIGHT = 1000
WIDTH = 1600
window = Tk()
window.title('DINO RUN')
c = Canvas(window, width=WIDTH, height=HEIGHT, bg='white')
c.pack()
figure = c.create_rectangle(150,650,200,800,fill="black")
trans = c.create_rectangle(0,0,0,0,width=0)
trans2 = c.create_rectangle(0,0,0,0,width=0)
x = 0
ground = c.create_rectangle(0,800,1600,1000,fill="black")
time = 0
size = tkFont.Font(size=100)
size2 = tkFont.Font(size=200)
score = c.create_text(1300,50,font=size)
old_time = 0
ids = []
speed = 1
stop = 0

def pressed(event):
    pos = c.coords(figure)
    if pos[3] >= 800:
        if event.keysym == 'space':
            c.move(trans,10,0)
c.bind_all('<space>',pressed)
def pressed(event):
    pos = c.coords(figure)
    if event.keysym == 'Down':
        c.move(trans2,-10,0)
    if pos[3] >= 800:
        if event.keysym == 'Up':
            c.move(trans,10,0)
c.bind_all('<Key>',pressed)


while True:
    window.update()   
    pos2 = c.coords(trans)
    pos3 = c.coords(trans2)
    speed += 0.001
    c.move(figure,0,-x)
    x -= 0.2
    pos = c.coords(figure)
    if pos[3] > 800:
        c.move(figure,0,-pos[3]+800)
        if pos2[0] >= 10:
            c.move(trans,-10,0)
            x = 11
    if pos3[0] <= -10:
        c.move(trans2,10,0)
        x = -20

    c.itemconfig(score, text=str(time))
    time += 1

    if time-old_time > 750/speed and randint(1,100) == 1:
        id = c.create_rectangle(1600,700,1650,800,fill="black")
        ids.append(id)
        old_time = time

    delete = []
    for i in range(len(ids)):
        c.move(ids[i],-speed,0)
        pos_id = c.coords(ids[i])
        if pos_id[2] < 100:
            delete.append(i)
        if pos_id[1] < pos[3] and pos_id[2] > pos[2] and pos_id[0] < pos[2] or pos_id[1] < pos[3] and pos_id[2] > pos[0] and pos_id[0] < pos[0]:
            stop = 1

    for x in range(len(delete)):
        c.delete(ids[delete[x]])
        ids.pop(delete[x])

    if stop == 1:
        print("STOP")
        break

c.create_text(WIDTH/2,HEIGHT/2,text="GAME OVER",font=size2)

while True:
    window.update()