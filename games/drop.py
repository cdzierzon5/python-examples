#Cody Dzierzon

from superwires import games, color
import random
SCORE = 0

games.init(screen_width= 800, screen_height= 533, fps= 50)

class Jedi(games.Sprite):
    def update(self):
        self.x = games.mouse.x
        self.y = 450
        self.check_collide()
    def check_collide(self):
        for laser in self.overlapping_sprites:
            laser.handle_collide()




class Bullet(games.Sprite):

    def handle_collide(self):
        self.x = random.randrange(games.screen.width)
        self.y = random.randrange(games.screen.height)

    def update(self):
        global SCORE
        # """Reverse a velocity component if edge of screen reached"""
        #bounce
        # if self.right > games.screen.width or self.left <0:
        #     self.dx = -self.dx
        #     SCORE+= 1
        # if self.bottom > games.screen.height or self.top<0:
        #     self.dy = -self.dy
        #     SCORE += 1
        #teleport / bounce
        if self.bottom > games.screen.height or self.top<0:
            self.dy = -self.dy
            SCORE += 1
        if self.left > games.screen.width:
            self.right = 0
            SCORE += 1

        if self.right < 0:
            self.left = games.screen.width
            SCORE += 1



class ScText(games.Text):
    def update(self):
        self.value = SCORE

def main():
    bg_img = games.load_image("images\death.jpg", transparent = False)
    laser_img = games.load_image("images\Bullet2.jpg", transparent=False)
    jedis_img = games.load_image("images\darth-removebg.png", transparent=True)
#added img to bg
    games.screen.background = bg_img
#create bullet
    laser = Bullet(image = laser_img,
                        x=games.screen.width/2,
                        y=games.screen.height/2,
                        dx = random.randint(-10,10),
                        dy = random.randint(-10,10))
    laser2 = Bullet(image=laser_img,
                   x=games.screen.width / 2,
                   y=games.screen.height / 2,
                   dx=random.randint(-10, 10),
                   dy=random.randint(-10, 10))
    laser3 = Bullet(image=laser_img,
                   x=games.screen.width / 2,
                   y=games.screen.height / 2,
                   dx=random.randint(-10, 10),
                   dy=random.randint(-10, 10))
    laser4 = Bullet(image=laser_img,
                   x=games.screen.width / 2,
                   y=games.screen.height / 2,
                   dx=random.randint(-10, 10),
                   dy=random.randint(-10, 10))
    laser5 = Bullet(image=laser_img,
                   x=games.screen.width / 2,
                   y=games.screen.height / 2,
                   dx=random.randint(-10, 10),
                   dy=random.randint(-10, 10))
    laser6 = Bullet(image=laser_img,
                    x=games.screen.width / 2,
                    y=games.screen.height / 2,
                    dx=random.randint(-10, 10),
                    dy=random.randint(-10, 10))
    laser7 = Bullet(image=laser_img,
                    x=games.screen.width / 2,
                    y=games.screen.height / 2,
                    dx=random.randint(-10, 10),
                    dy=random.randint(-10, 10))
    laser8 = Bullet(image=laser_img,
                    x=games.screen.width / 2,
                    y=games.screen.height / 2,
                    dx=random.randint(-10, 10),
                    dy=random.randint(-10, 10))
    laser9 = Bullet(image=laser_img,
                   x=games.screen.width / 2,
                   y=games.screen.height / 2,
                   dx=random.randint(-10, 10),
                   dy=random.randint(-10, 10))
    laser10 = Bullet(image=laser_img,
                    x=games.screen.width / 2,
                    y=games.screen.height / 2,
                    dx=random.randint(-10, 10),
                    dy=random.randint(-10, 10))
    laser11 = Bullet(image=laser_img,
                    x=games.screen.width / 2,
                    y=games.screen.height / 2,
                    dx=random.randint(-10, 10),
                    dy=random.randint(-10, 10))
    laser12 = Bullet(image=laser_img,
                    x=games.screen.width / 2,
                    y=games.screen.height / 2,
                    dx=random.randint(-10, 10),
                    dy=random.randint(-10, 10))
    laser13 = Bullet(image=laser_img,
                    x=games.screen.width / 2,
                    y=games.screen.height / 2,
                    dx=random.randint(-10, 10),
                    dy=random.randint(-10, 10))
    laser14 = Bullet(image=laser_img,
                    x=games.screen.width / 2,
                    y=games.screen.height / 2,
                    dx=random.randint(-10, 10),
                    dy=random.randint(-10, 10))
    laser15 = Bullet(image=laser_img,
                    x=games.screen.width / 2,
                    y=games.screen.height / 2,
                    dx=random.randint(-10, 10),
                    dy=random.randint(-10, 10))
    laser16 = Bullet(image=laser_img,
                    x=games.screen.width / 2,
                    y=games.screen.height / 2,
                    dx=random.randint(-10, 10),
                    dy=random.randint(-10, 10))
    #create jedi
    the_jedi = Jedi(image= jedis_img,
                    x = games.mouse.x,
                    y = games.mouse.y)
#creates text obj
    score = ScText(value = SCORE,
                   is_collideable= False,
                    size = 60,
                    color = color.red,
                    x = 700,y = 30)

    games.screen.add(laser)
    games.screen.add(laser2)
    games.screen.add(laser3)
    games.screen.add(laser4)
    games.screen.add(laser5)
    games.screen.add(laser6)
    games.screen.add(laser7)
    games.screen.add(laser8)
    games.screen.add(laser9)
    games.screen.add(laser10)
    games.screen.add(laser11)
    games.screen.add(laser12)
    games.screen.add(laser13)
    games.screen.add(laser14)
    games.screen.add(laser15)
    games.screen.add(laser16)
    games.screen.add(the_jedi)
    games.screen.add(score)

    games.mouse.is_visible = False
    games.screen.event_grab = True

# game_over = games.Message(value = "Game Over",
#                           size = 100,
#                           color = color.red,
#                           x = games.screen.width/2,
#                           y = games.screen.height/2,
#                           lifetime = 250,
#                           after_death = games.screen.quit)
# games.screen.add(game_over)

    games.screen.mainloop()
main()