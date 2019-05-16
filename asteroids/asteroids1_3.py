#asteroids 1.0
#Cody Dzierzon
#4/19

#imports
from superwires import games, color
import random
import math

#Global info
games.init(screen_width = 640, screen_height = 480, fps = 60)



#Classes
class Game(object):
    def __init__(self):
        #set level
        self.level = 0
        #load sound for level advance
        self.sound = games.load_sound("Music/level.wav")
        #create score
        self.score = games.Text(value = 0,
                                size= 20,
                                color = color.white,
                                top = 5,
                                right = games.screen.width - 10,
                                is_collideable = False)
        games.screen.add(self.score)

        self.lives = games.Text(value= 3,
                                size=20,
                                color=color.white,
                                top=5,
                                right= 10,
                                is_collideable=False)
        games.screen.add(self.lives)


        #create players ship
        self.ship = Ship(game = self,
                           x = games.screen.width/2,
                           y = games.screen.height/2)
        games.screen.add(self.ship)
    def play(self):
        games.music.load("Music/theme.mid")
        games.music.play(-1)

        bg_img = games.load_image("images/Space.png")
        games.screen.background = bg_img

        self.advance()

        games.screen.mainloop()

    def advance(self):
        self.level += 1
        # amount of space around ship when creating asteroids
        BUFFER = 150

        #Create objects
        for i in range(self.level):
            x_min = random.randrange(BUFFER)
            y_min = BUFFER - x_min

            x_distance = random.randrange(x_min, games.screen.width - x_min)
            y_distance = random.randrange(y_min, games.screen.height - y_min)

            x = self.ship.x + x_distance
            y = self.ship.y + y_distance

            x %= games.screen.width
            y %= games.screen.height

            new_asteroid = Asteroid(game = self, x = x, y = y, size = Asteroid.LARGE)
            games.screen.add(new_asteroid)

        #display level number
        level_message = games.Message(value = "Level" + str(self.level),
                                      size = 40,
                                      color = color.green,
                                      x = games.screen.width/2,
                                      y = games.screen.height/10,
                                      lifetime= 3 * games.screen.fps,
                                      is_collideable = False)
        games.screen.add(level_message)

        if self.level > 1:
            self.sound.play()

    def end(self):
        """End of the game"""
        # LIVES = 3
        # if LIVES != 0:
        #     LIVES -= 1
        #     self.Ship()
        # if LIVES == 0:
        end_message = games.Message(value = "Game Over",
                                    size = 90,
                                    color = color.green,
                                    x = games.screen.width/2,
                                    y = games.screen.height/2,
                                    lifetime= 5 * games.screen.fps,
                                    after_death = games.screen.quit,
                                    is_collideable = False)
        games.screen.add(end_message)



class Wrapper(games.Sprite):
    def update(self):
        if self.left > games.screen.width:
            self.right = 0
        if self.right < 0:
            self.left = games.screen.width
        if self.top > games.screen.height:
            self.bottom = 0
        if self.bottom< 0:
            self.top = games.screen.height

    def die(self):
        self.destroy()

class Collider(Wrapper):
    def update(self):
        """check for overlapping sprites"""
        super(Collider, self).update()

        if self.overlapping_sprites:
            for sprite in self.overlapping_sprites:
                sprite.die()
            self.die()

    def die(self):
        #create explosion
        new_explosion = Explosion(obj_x= self.x, obj_y= self.y)
        games.screen.add(new_explosion)
        self.destroy()


class Asteroid(Wrapper):
    SMALL = 1
    MEDIUM = 2
    LARGE = 3
    images = {SMALL : games.load_image("images/asmall.png"),
              MEDIUM: games.load_image("images/amed.png"),
              LARGE: games.load_image("images/alarge.png"),}
    SPEED = 2
    SPAWN = 2
    POINTS = 30
    total = 0

    def __init__(self, game, x, y, size):
        Asteroid.total += 1

        super(Asteroid, self).__init__(image= Asteroid.images[size],
                                       x = x,
                                       y = y,
                                       dx = random.choice([1, -1]) * Asteroid.SPEED * random.random() / size,
                                       dy = random.choice([1, -1]) * Asteroid.SPEED * random.random() / size)
        self.size = size
        self.game = game

    def die(self):
        #if asteroid isn't small, replace with two smaller asteroid
        Asteroid.total -= 1
        #add to score
        self.game.score.value += int(Asteroid.POINTS/self.size)
        self.game.score.right = games.screen.width - 10

        if self.size != Asteroid.SMALL:
            for i in range(Asteroid.SPAWN):
                new_asteroid = Asteroid(game = self.game,
                                        x = self.x,
                                        y = self.y,
                                        size = self.size - 1)
                games.screen.add(new_asteroid)

        if Asteroid.total == 0:
            self.game.advance()
        super(Asteroid, self).die()

class Ship(Collider):
    image = games.load_image("images/pixelship2.png")
    sound = games.load_sound("Music/thrust.wav")

    ROTATION_STEP = 6
    VELOCITY_STEP = .03
    MISSILE_DELAY = 25
    VELOCITY_MAX = 3

    def __init__(self, game, x, y):
        super(Ship,self).__init__(image = Ship.image,
                                  x = x,
                                  y = y)
        self.game = game
        self.missile_wait = 0

    def update(self):
        super(Ship, self).update()
        if games.keyboard.is_pressed(games.K_a) or games.keyboard.is_pressed(games.K_LEFT):
            self.angle -= Ship.ROTATION_STEP

        if games.keyboard.is_pressed(games.K_d) or games.keyboard.is_pressed(games.K_RIGHT):
            self.angle += Ship.ROTATION_STEP

        if games.keyboard.is_pressed(games.K_w) or games.keyboard.is_pressed(games.K_UP):
            Ship.sound.play()
            angle = self.angle * math.pi/180
            self.dx += Ship.VELOCITY_STEP * math.sin(angle)
            self.dy += Ship.VELOCITY_STEP * -math.cos(angle)
            self.dx = min(max(self.dx, -Ship.VELOCITY_MAX), Ship.VELOCITY_MAX)
            self.dy = min(max(self.dy, -Ship.VELOCITY_MAX), Ship.VELOCITY_MAX)

        if self.missile_wait > 0:
            self.missile_wait -= 1


        if games.keyboard.is_pressed(games.K_SPACE) and self.missile_wait == 0:
            new_missile = Missile(self.x, self.y, self.angle)
            games.screen.add(new_missile)
            self.missile_wait = Ship.MISSILE_DELAY

    def die(self):
        """Destroy ship at the end of the game"""
        self.game.end()
        super(Ship, self).die()






class Missile(Collider):
    image = games.load_image("images/dot2.png")
    sound = games.load_sound("Music/Shoot7.wav")
    BUFFER = 60
    VELOCITY_FACTOR = 10
    LIFETIME = 35
    def __init__(self,ship_x,ship_y,ship_angle):
        Missile.sound.play()
        angle = ship_angle * math.pi /180


        #calculate missles starting position
        buffer_x = Missile.BUFFER * math.sin(angle)
        buffer_y = Missile.BUFFER * -math.cos(angle)

        x = ship_x + buffer_x
        y = ship_y + buffer_y

        dx = Missile.VELOCITY_FACTOR * math.sin(angle)
        dy = Missile.VELOCITY_FACTOR * -math.cos(angle)

        super(Missile,self).__init__(image = Missile.image,
                                     x = x,
                                     y = y,
                                     dx = dx,
                                     dy = dy)
        self.lifetime = Missile.LIFETIME

    def update(self):
        super(Missile, self).update()

        self.lifetime -= 1
        if self.lifetime == 0:
            self.destroy()

class Ufo(Collider):
    ufo_image = games.load_image("images/ufo2.png")
    def __init__(self,game,player):
        super(Ufo, self).__init__(image = ufo_image,
                                x = games.screen.width,
                                y = 0,
                                dx = random.randint(-5, 5),
                                dy = random.randint(-5, 5))
        self.bullet_wait = 100
        self.game = game
        self.player = player
        self.angle = 200

    def update(self):
        if self.right <0:
            self.destroy()
        self.bullet_wait -= 1
        if self.bullet_wait == 0:
            self.bullet_wait = 100
            self.shoot()

    def shoot(self):
        if self.player.x < self.x and self.player.y < self.y:
            self.angle = random.randint(270,360)
        if self.player.x < self.x and self.player.y > self.y:
            self.angle = random.randint(180,270)
        if self.player.x > self.x and self.player.y < self.y:
            self.angle = random.randint(0,90)
        if self.player.x > self.x and self.player.y > self.y:
            self.angle = random.randint(90, 180)

        shot = Missile(self.x, self.y, self.angle)
        games.screen.add(shot)

    def die(self):
        self.game.score.value += 500
        self.game.ufocheck()
        Wrapper.die(self)


class Explosion(games.Animation):
    sound = games.load_sound("Music/explosion1.wav")
    exp_images = ["images/boom1.png",
              "images/boom2.png",
              "images/boom3.png",
              "images/boom4.png",
              "images/boom5.png",
              "images/boom6.png"]
    def __init__(self, obj_x, obj_y):
        super(Explosion, self).__init__(images = Explosion.exp_images,
                                        x = obj_x,
                                        y = obj_y,
                                        repeat_interval= 5,
                                        n_repeats= 1,
                                        is_collideable= False)
        Explosion.sound.play()







#main
def main():
    asteroids = Game()
    asteroids.play()

main()