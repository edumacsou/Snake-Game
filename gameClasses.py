import pygame, os, random, math

class Fruit(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(my_path('fruit.png'))
        self.rect = self.image.get_rect()
        position = (random.randrange(10, 770, 20),random.randrange(90, 570, 20))
        self.rect.left, self.rect.top = position

class Segment(pygame.sprite.Sprite):
    def __init__(self, image_file, position):
        pygame.sprite.Sprite.__init__(self)  #call Sprite initializer
        self.image = pygame.image.load(image_file)
        self.rect = self.image.get_rect()
        self.rect.left, self.rect.top = position

class Button(pygame.sprite.Sprite):
    def __init__(self, image_file_1, image_file_2):
        pygame.sprite.Sprite.__init__(self)  #call Sprite initializer
        position = (315, 450)
        size = (170, 70)
        
        self.image_mouse_off = pygame.image.load(my_path(image_file_1))
        self.image_mouse_on = pygame.image.load(my_path(image_file_2))

        self.rect = pygame.Rect(position, size)

class Background(pygame.sprite.Sprite):
    def __init__(self, image_file):
        pygame.sprite.Sprite.__init__(self)  #call Sprite initializer
        self.image = pygame.image.load(my_path(image_file))
        self.rect = self.image.get_rect()
        self.rect.left, self.rect.top = 0, 0

class snake():
    def __init__(self, position):
        size = 20, 20
        self.segments = []
        self.segments.append(Segment(my_path('head.png'), position))
        self.speed = 0.3
        self.score = 0

    def draw(self, screen):
        for segment in reversed(self.segments):
            screen.blit(segment.image, segment.rect)
    
    def move(self, movement):
        for index in range(len(self.segments)-1, 0, -1):
            self.segments[index].rect.topleft = self.segments[index-1].rect.topleft
        self.segments[0].rect = self.segments[0].rect.move(movement)

    def add(self):
        position = self.segments[len(self.segments)-1].rect.topleft
        self.segments.append(Segment(my_path('body.png'), position))
        self.score += 1
        self.accelerate()

    def accelerate(self):
        if self.score <= 25: self.speed = speed_function(self.score)
        else: self.speed = 0.1

def my_path(file_name):
    dir = os.path.dirname(os.path.abspath(__file__))
    return os.path.join(dir + "\Samples\\" + file_name)

def speed_function(score):
    return 1/(3*math.exp(score/20))

def direction(event_key, movement, player):
    moves = {pygame.K_UP: (0, -20), pygame.K_DOWN: (0, 20), pygame.K_RIGHT: (20, 0), pygame.K_LEFT: (-20, 0)}

    if len(player.segments) > 1 and player.segments[0].rect.move(moves.get(event_key, (movement))).topleft == player.segments[1].rect.topleft : return movement

    return moves.get(event_key, (movement))

def is_player_dead(player):
    if (player.segments[0].rect.right > 800
        or player.segments[0].rect.left < 0
        or player.segments[0].rect.top < 90
        or player.segments[0].rect.bottom > 600):
        return True

    for segment in player.segments[1:]:
        if player.segments[0].rect.center == segment.rect.center: return True
    
    return False