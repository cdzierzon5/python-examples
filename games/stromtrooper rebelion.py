#Stormtrooper Rebelion
#Cody Dzierzon
#4/19


#imports
from superwires import games, color
import random

#global variables
games.init(screen_width= 800, screen_height= 533, fps= 60)
SCORE = 0
Lives = 3


#Classes
class Trooper(games.Sprite):
    image = games.load_image("images\storm.png", transparent=True)

    def __init__(self, y = 60, speed = 5, odds_change = 50):
        super(Trooper, self).__init__(image = Trooper.image,
                                      x = games.screen.width/2,
                                      y = y,
                                      dx = speed)
        self.odds_change = odds_change
        self.time_til_drop = 0

    def update(self):
        if self.left < 0 or self.right > games.screen.width:
            self.dx = -self.dx
        elif random.randrange(self.odds_change) == 0:
            self.dx = -self.dx

        self.check_drop()


    def check_drop(self):
        if self.time_til_drop > 0:
            self.time_til_drop -= 1
        else:
            new_laser = Laser(x = self.x)
            games.screen.add(new_laser)
            self.time_til_drop = random.randint(60,300)



class Vader(games.Sprite):
    image = games.load_image("images\darth-removebg.png", transparent=True)

    def __init__(self):
        super(Vader, self).__init__(image = Vader.image,
                                    x = games.mouse.x,
                                    bottom= games.screen.height)

    def update(self):
        self.x = games.mouse.x

        if self.left < 0:
            self.left = 0

        if self.right > games.screen.width:
            self.right = games.screen.width

        self.check_catch()

    def check_catch(self):
        for Laser in self.overlapping_sprites:
            #add to sore()
            Laser.handle_caught()

class Laser(games.Sprite):
    image = games.load_image("images\Bullet2.jpg")
    speed = 15

    def __init__(self, x, y= 90, speed = random.randrange(speed)+1):
        super(Laser,self).__init__(image = Laser.image, x=x, y=y, dy = speed)

    def update(self):
        if self.top > games.screen.height:
            self.destroy()
            Lives -= 1
            self.end_game()
    if Lives == 0:
        def end_game(self):
            """End the Game"""
            end_message = games.Message(value + "Game Over",
                                        size = 90,
                                        color = color.red,
                                        x = games.screen.width/2,
                                        y = games.screen.width/2,
                                        lifetime = 5 * games.screen.fps,
                                        after_death = games.screen.quit)
            games.screen.add(end_message)

    def handle_caught(self):
        self.destroy()


class ScText(games.Text):
    def update(self):
        self.value = SCORE
        self.valus = Lives


#main
def main():


#load Data
    bg_img = games.load_image("images\death.jpg", transparent = False)

#create objects
    the_vader = Vader()
    the_trooper = Trooper()
    score = ScText(value=SCORE,
                       is_collideable=False,
                       size=60,
                       color=color.red,
                       x=750, y=30)

    lives = ScText(value=Lives,
                           is_collideable=False,
                           size=60,
                           color=color.red,
                           x=20, y=30)

#draw
    games.screen.background = bg_img
    games.screen.add(the_vader)
    games.screen.add(the_trooper)
    games.screen.add(score)
    games.screen.add(lives)

#game setup
    games.mouse.is_visible = False
    games.screen.event_grab = True

#start loop
    games.screen.mainloop()

#starting point
main()

