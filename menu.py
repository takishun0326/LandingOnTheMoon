import pgzrun
import random

WIDTH = 400
HEIGHT = 600

rocket = Actor('rocket', center = (200,300))

stars = []
for i in range(20):
    rect = Rect((random.randrange(WIDTH), random.randrange(HEIGHT)), (2,2))
    stars.append(rect)

speed = 0           #speed
acceleration = 0.1  #acce
key_flg = False     #UPkey Press flg
status = 0          #0:Menu, 1:Game 2:GameClear, 3:GameOver

anime_r = animate(None)

def draw():
    global status
    
    screen.clear()
    for i in range(20):
        screen.draw.rect(stars[i], 'WHITE')
    
    for i in range(50):
        screen.draw.line((150-i*3,550+i), (250+i*3, 550+i), (128,128,128))
    
    # Menu
    if status == 0:
        for i in range(10):
            screen.draw.circle(rocket.midbottom, i+1, (255, i *20, 0))
            screen.draw.text('Landing on The Moon' , (80,100), owidth=1.5, ocolor='YELLOW', color='BLACK', fontsize = 32)
    # Game
    elif status == 1:
        if key_flg: # UPkey Pressed 
            for i in range(10):
                screen.draw.circle(rocket.midbottom, i+1, (255, i*20, 0))
    
    #GameClear
    elif status == 2: 
        screen.draw.text('GAME CLEAR', (40,300), owidth = 1.5, ocolor = 'YELLOW', color = 'BLACK', fontsize=64)
    
    else :
        screen.draw.text('GAME OVER', (40, 300), owidth = 1.5, ocolor = 'YELLOW', color = 'BLACK', fontsize=64)
    
    rocket.draw()


def on_key_down(key):
    global status, speed, acceleration
    if key == keys.SPACE and anime_r.running != True:
        if status == 0 or status == 2 or status == 3:
            status = 1
            rocket.y = 200
            speed = 0
            acceleration = 0.1
            rocket.angle = 0

def update():
    global speed, acceleration, status, key_flg, anime_r
    if status == 1:
        if keyboard.up:
            key_flg = True
            acceleration = -0.1
        else :
            key_flg = False
            acceleration = 0.1
        
        speed += acceleration
        rocket.y += speed
        if rocket.y > 500:
            if speed < 1.0:
                status = 2
            else :
                status = 3
                anime_r = animate(rocket, 'bounce_start_end', 1, angle=45)
        


pgzrun.go()