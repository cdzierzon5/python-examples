#asteroids 1.0
#Cody Dzierzon
#4/19

#imports
from superwires import games
import random

#Global info
games.init(screen_width = 640, screen_height = 480, fps = 60)



#Classes

class Asteroid(games.Sprite):
    SMALL = 1
    MEDIUM = 2
    LARGE = 3
    images = {SMALL : games.load_image("images/asmall.png"),
              MEDIUM: games.load_image("images/amed.png"),
              LARGE: games.load_image("images/alarge.png"),}
    SPEED = 2

    def __init__(self, x, y, size):
        super(Asteroid, self).__init__(image= Asteroid.images[size],
                                       x = x,
                                       y = y,
                                       dx = random.choice([1, -1]) * Asteroid.SPEED * random.random() / size,
                                       dy = random.choice([1, -1]) * Asteroid.SPEED * random.random() / size)
        self.size = size
    def update(self):
        if self.left > games.screen.width:
            self.right = 0
        if self.right < 0:
            self.left = games.screen.width
        if self.bottom > games.screen.height:
            self.top = 0
        if self.top < 0:
            self.bottom = games.screen.height




#main
def main():

    #load data
    bg_img = games.load_image("images/Space.png")



    #Create objects
    for i in range(8):
        x = random.randrange(games.screen.width)
        y = random.randrange(games.screen.height)
        size = random.choice([Asteroid.SMALL, Asteroid.MEDIUM, Asteroid.LARGE])
        new_asteroid = Asteroid(x=x,y=y,size=size)
        games.screen.add(new_asteroid)




    #draw objects
    games.screen.background = bg_img




    #game setup





    #start main loop
    games.screen.mainloop()

main()