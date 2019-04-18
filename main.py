import pygame
import random
# Layout
# Logik i spel



class Snake():
    def __init__(self, head = [30,10]):
        self.head = head #[X1, Y1]
        self.body = [head, [head[0] - 10, head[1]], [head[0] - 20, head[1]]] #[[X1,Y1], [X2, Y2], ]
        self.lenth = len(self.body)
        self.dir = pygame.K_RIGHT
        self.bodySize = 9

    def newPosition(self,key):
        self.dir = key
        if key == pygame.K_LEFT:
            self.head = [self.head[0] - 10, self.head[1]]

        elif key == pygame.K_RIGHT:
            self.head = [self.head[0] + 10, self.head[1]]

        elif key == pygame.K_UP:
            self.head = [self.head[0], self.head[1] - 10]
        elif key == pygame.K_DOWN:
            self.head = [self.head[0], self.head[1] + 10]

        self.body = [self.head] + self.body[:-1]



    def checkValid(self, screen_width, screen_height):
        for bodyPart in self.body[1:]:
            if self.head == bodyPart:
                return False

        if self.head[0] >= screen_width or self.head[0] < 0:
            return False

        elif self.head[1] >= screen_height or self.head[1] < 0:
            return False

    def haveEaten(self, foodCord):
        if self.head == foodCord:
            self.body = self.body + [[0,0]]
            return True

        return False

    def oppositeKey(self, key):
        if self.dir == pygame.K_RIGHT and key == pygame.K_LEFT:
            key = pygame.K_RIGHT

        if self.dir == pygame.K_LEFT and key == pygame.K_RIGHT:
            key = pygame.K_LEFT

        if self.dir == pygame.K_UP and key == pygame.K_DOWN:
            key = pygame.K_UP
        if self.dir == pygame.K_DOWN and key == pygame.K_UP:
            key = pygame.K_DOWN

        return key

class Food():
    def __init__(self):
        self.cord = [0,0]

    def update(self, screen_width, screen_height, body):
        self.cord = [random.randrange(0, screen_width, 10), random.randrange(0, screen_height, 10)]
        if self.cord in body:
            self.update(screen_width, screen_height, body)


def display():
    theSnake = Snake()
    screen_width=400
    screen_height=400
    apple = Food()
    apple.update(screen_width, screen_height, theSnake.body)
    pygame.init()

    pygame.display.set_caption("Snake")
    displayMode = pygame.display.set_mode((screen_width,screen_height))
    run = True
    key = pygame.K_RIGHT
    print(key)
    while run:
        displayMode.fill((0,0,0))
        pygame.time.delay(100)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

            if event.type == pygame.KEYDOWN:
                key = event.key
                key = theSnake.oppositeKey(key)


        for bodyPart in theSnake.body:
            pygame.draw.rect(displayMode, (255,255,255), (bodyPart[0], bodyPart[1], theSnake.bodySize, theSnake.bodySize))

        pygame.draw.rect(displayMode, (255,0,0), (apple.cord[0], apple.cord[1], theSnake.bodySize, theSnake.bodySize))
        if theSnake.haveEaten(apple.cord):
            apple.update(screen_width, screen_height, theSnake.body)
        theSnake.newPosition(key)
        if theSnake.checkValid(screen_width, screen_height) == False:
            run = False

        pygame.display.update()




def main():
    display()

if __name__ == '__main__':
    main()
