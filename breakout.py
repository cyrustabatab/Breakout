import pygame
import random

pygame.init()


class Ball:

    def __init__(self,x,y,size):
        self.x = x
        self.y = y
        self.size = size
        self.rect = pygame.Rect(self.x,self.y,self.size,self.size)
        self.x_speed = random.choice([-2,2])
        self.y_speed = -2

    def draw(self):
        pygame.draw.rect(screen,(255,255,255),self.rect)

    def move(self,blocks,paddle):

        self.rect.x += self.x_speed
        self.rect.y += self.y_speed
        
            


        if self.rect.x <= 0 or self.rect.x >= 724- self.size:
            self.x_speed = -self.x_speed
        elif self.rect.y <= 0 or self.rect.y >= 400 - self.size:
            self.y_speed = -self.y_speed
        elif self.rect.colliderect(paddle.rect):
            if self.rect.left == paddle.rect.right - abs(self.x_speed):
                self.x_speed = -self.x_speed
            elif self.rect.right == paddle.rect.left + abs(self.x_speed):
                self.x_speed = -self.x_speed
                print('here4')
            else:
                self.y_speed = -self.y_speed
        else:
            for block in list(blocks):
                if self.rect.colliderect(block.rect):
                    if self.rect.left == block.rect.right - abs(self.x_speed):
                        self.x_speed = -self.x_speed

                        print('here')
                    elif self.rect.right == block.rect.left + abs(self.x_speed):
                        self.x_speed = -self.x_speed
                        print('here2')
                    else:
                        self.y_speed = -self.y_speed

                    blocks.remove(block)





class Block:

  def __init__(self,x,y,width,height,color):
    self.x = x
    self.y = y
    self.height = height
    self.width =width
    self.color = color
    self.rect = pygame.Rect(self.x,self.y,self.width,self.height)
  
  def draw(self):
    pygame.draw.rect(screen,self.color,self.rect)
class Paddle:

  def __init__(self,x,y,width,height,speed):
    self.x = x
    self.y = y
    self.width = width
    self.height = height
    self.rect = pygame.Rect(self.x,self.y,self.width,self.height)
    self.speed = speed
  
  def move(self,pressed_keys):

    if pressed_keys[pygame.K_LEFT] == True:
      self.rect.x -= self.speed
    if pressed_keys[pygame.K_RIGHT] == True:
      self.rect.x += self.speed

    if self.rect.x <= 0:
      self.rect.x = 0
    
    if self.rect.x >= 724 - self.width:
      self.rect.x = 724 - self.width
  
  def draw(self):

    pygame.draw.rect(screen,(255,255,255),self.rect)
screen = pygame.display.set_mode((724,400))
clock = pygame.time.Clock()
done = False
paddle = Paddle(200,380,60,10,4)
ball = Ball(200,370,10)
blocks = []

rows = 10
columns = 12
block_width = 50
block_height = 25


def generate_blocks():
    blocks = []
    for i in range(rows):
      for j in range(columns):
        color = (random.randint(1,254),random.randint(1,254),random.randint(1,254))
        block = Block(((block_width + 2) * j) + 50,((block_height + 2) * i) + 25,block_width,block_height,color)
        blocks.append(block)
    return blocks

blocks = generate_blocks()


while done == False:
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      done = True
  

  pressed_keys = pygame.key.get_pressed()

  paddle.move(pressed_keys)
  ball.move(blocks,paddle)

  screen.fill((0,0,0))
  for block in blocks:
      block.draw()
  paddle.draw()
  ball.draw()
  pygame.display.update()
  clock.tick(60)
