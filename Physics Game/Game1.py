import pygame
from pygame.math import Vector2

class Avatar(object):
    def __init__(self):
        self.width = 50
        self.height = 50
        self.xDirection = 0
        self.xDirectionStep = -1
        self.numberStep = 0
        self.numberStep = 0
        self.maxVelocity = 200
        self.isJumping = False

        self.velocity = Vector2()
        self.velocityStep = Vector2()
        self.position = Vector2(20, 0)
        self.positionPrev = Vector2()
        self.positionStep = Vector2()

        self.mass = BaselineParams.avatarWeight
        self.image = pygame.image.load('hero.png')
        self.image = pygame.transform.scale(self.image, (50, 50))

    def jumpHero(self):
        if self.isJumping == False:
            self.isJumping = True

    def drawDisplay(self, gameDisplay):
        if self.xDirection != self.xDirectionStep and self.xDirection != 0:
            self.image = pygame.transform.flip(self.image, True, False)

        if self.xDirection != 0:
            self.xDirectionStep = self.xDirection

        posDraw = Vector2(self.position.x - self.width / 2, self.position.y - self.height)
        gameDisplay.blit(self.image, posDraw)

    def calculateMovement(self, force, timeStep):
        acceleration = force / self.mass
        self.velocityStep = self.velocity + acceleration * timeStep
        self.positionStep = self.position + self.velocityStep * timeStep

    def moveHero(self):
        self.positionPrev = self.position
        self.position = self.positionStep
        self.velocity = self.velocityStep
        self.numberStep += 1


class BaselineParams(object):
    airFriction = 2
    friction = 2
    gravity = Vector2(0, 981)  # g = 9.81
    avatarWeight = 1
    fps = 60.0
    freq = 1.0 / fps
    recalculationFreq = freq / 32  # Relalculations over frame
    jumpForce = Vector2(0, -800 / recalculationFreq)


class Platforms(object):
    def __init__(self, position, size=Vector2(64, 64)):
        self.image = pygame.image.load('Platform.png')
        self.image = pygame.transform.scale(self.image, (int(size.x), int(size.y)))
        self.width = size.x
        self.height = size.y
        self.position = position
        self.isCollided = False

    def drawDisplay(self, gameDisplay):
        gameDisplay.blit(self.image, self.position)

    def collides(self, Avatar):

        pos = self.position
        w = self.width
        h = self.height
        platformLeftCollider = pos.x
        platformRightCollider = pos.x + w
        platformBottomCollider = pos.y
        platformTopCollider = pos.y + h

        pos = Avatar.position
        w = Avatar.width
        h = Avatar.height
        AvatarLeftCollider = pos.x - w / 2
        AvatarRightCollider = pos.x + w / 2
        AvatarBottomCollider = pos.y - h
        AvatarTopCollider = pos.y


        if (AvatarRightCollider < platformLeftCollider or AvatarLeftCollider > platformRightCollider \
                or AvatarBottomCollider > platformTopCollider or AvatarTopCollider < platformBottomCollider):
            return False
        else:
            return True

    def AvatarOn(self, Avatar):
        return (self.position.x - Avatar.width / 2.0 < Avatar.position.x < self.position.x + self.width + Avatar.width / 2.0) \
               and (self.position.y < Avatar.position.y < self.position.y + self.height / 3.0) and Avatar.velocity.y > 0


class Game(object):
    def __init__(self):

        pygame.init()

        self.bg_image = pygame.image.load('background.png')
        self.display_width = 1280
        self.display_height = 580
        self.gameDisplay = pygame.display.set_mode((self.display_width, self.display_height))
        self.clock = pygame.time.Clock()
        self.playGame = True
        self.gameOver = False
        self.Avatar = Avatar()
        self.platforms = [Platforms(Vector2(10, 200), size=Vector2(164, 50)),
                          Platforms(Vector2(200, 410), size=Vector2(128, 50)),
                          Platforms(Vector2(380, 310), size=Vector2(128, 50)),
                          Platforms(Vector2(580, 310), size=Vector2(128, 50)),
                          Platforms(Vector2(850, 220), size=Vector2(164, 50)),
                          Platforms(Vector2(1100, 460), size=Vector2(196, 50))]

    def Physics(self):
        Avatar = self.Avatar
        force = BaselineParams.gravity * Avatar.mass

        if Avatar.isJumping:
            force += BaselineParams.jumpForce
            Avatar.isJumping = False

        if Avatar.xDirection == 0:
            force.x += Avatar.velocity.x * (-2 * BaselineParams.friction)

        if Avatar.velocity.y != 0:
            force -= BaselineParams.airFriction * Avatar.velocity

        walk_force = Vector2(Avatar.xDirection * 1000, 0)
        force += walk_force / 4  # Damping the acceleration
        Avatar.velocityStep.x = max(min(Avatar.velocity.x, Avatar.maxVelocity), -Avatar.maxVelocity)

        return force

    def Colliders(self):
        Avatar = self.Avatar
        for Platforms in self.platforms:
            if Platforms.collides(Avatar):
                if Platforms.AvatarOn(Avatar):
                    Avatar.position.y = Platforms.position.y
                    Avatar.velocity.y = 0
                else:
                    Avatar.velocity.x = 0
                    Avatar.velocity.y = 0
                    if Platforms.isCollided:
                        continue
                    else:
                        Platforms.isCollided = True
            else:
                Platforms.isCollided = False

        floor_y = self.display_height - 70
        if Avatar.position.y > floor_y:
            Avatar.position.y = floor_y
            Avatar.velocity.y = 0
            self.gameOver = True


    def game_loop(self):
        currentFrame = 0.0
        while self.playGame:
            self.Avatar.force = Vector2()
            currentFrame += BaselineParams.freq
            iteration = 32
            Avatar = self.Avatar
            self.gameDisplay.fill([0, 0, 0])
            self.gameDisplay.blit(self.bg_image, (0, 0))
            for Platforms in self.platforms:
                Platforms.drawDisplay(self.gameDisplay) # Need to reference platforms class here
            self.Avatar.drawDisplay(self.gameDisplay)

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_LEFT:
                        self.Avatar.xDirection = -1

                    if event.key == pygame.K_RIGHT:
                        self.Avatar.xDirection = 1

                    if event.key == pygame.K_UP:
                        self.Avatar.jumpHero()

                if event.type == pygame.QUIT:
                    self.playGame = False

                if event.type == pygame.KEYUP:
                    if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                        self.Avatar.xDirection = 0

            while iteration != 0:
                force = self.Physics()
                Avatar.calculateMovement(force, BaselineParams.recalculationFreq)
                Avatar.moveHero()
                self.Colliders()
                iteration -= 1

            if (Avatar.position.x - Avatar.width / 2.0 <= 0 and Avatar.xDirection < 0) \
                    or (Avatar.position.x + Avatar.width / 2.0 >= self.display_width and Avatar.xDirection > 0):
                Avatar.xDirection = 0
                Avatar.velocity.x = 0

            pygame.display.update()
            self.clock.tick(BaselineParams.fps)


game = Game()
while(not game.gameOver):
   game.game_loop()
pygame.quit()
quit()
