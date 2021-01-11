#Import necessary modules
import os
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "hide" #Hide the starting intialize text
import random #Get random values
import pygame #Module for creating games
import math #For applying math
import time #To measure time

# Intialize pygame
pygame.init()

# create the screen
screen = pygame.display.set_mode((480, 480))

# Background
background = pygame.image.load('floor.png')
#Uranium
uranium = pygame.image.load('uranium.png')

#Define color codes in RGB for text background and colour
black = (0, 0, 0)
white = (255, 255, 255)

#Define font size and write out the rules
font = pygame.font.Font('freesansbold.ttf', 11)
text1 = font.render('CONTROLS: ARROW KEYS TO MOVE AND SPACE TO SHOOT', True, black, white)
text2 = font.render('OBJECTIVE: GET THE URANIUM AT THE END OF THE HALL', True, black, white)

pygame.display.set_caption("Perspectives") #Game title
icon = pygame.image.load('hero.png') #Image icon
pygame.display.set_icon(icon) #Set icon

playerImg = pygame.image.load('hero.png') #Load in the image of the player
playerX = 400 #Player starting coordinates
playerY = 400
playerX_change = 0
playerY_change = 0

# Enemy
enemyImg = []
enemyX = []
enemyY = []
enemyX_change = []
enemyY_change = []
num_of_enemies = 20

#Load in the bullet
bulletImg = pygame.image.load('bullet.png')
bulletX = 0
bulletY = 480
bulletX_change = 0
bulletY_change = 10
bullet_state = "ready"

for i in range(num_of_enemies): #Load number of enemies in a for loop
    enemyImg.append(pygame.image.load('enemy.png'))
    enemyX.append(random.randint(0, 480)) #Spawn enemy at random x coordinate
    enemyY.append(random.randint(50, 150)) #Spawn enemy at random y coordinate
    enemyX_change.append(1)
    enemyY_change.append(20)


def player(x, y): #define function to place hero in certain coordinates
    screen.blit(playerImg, (x, y)) #scree.blit places image on the screen


def enemy(x, y, i): #define function to place enemy in certain coordinates
    screen.blit(enemyImg[i], (x, y))

def fire_bullet(x, y): #Define a function to fire the bullet
    global bullet_state
    bullet_state = "fire"
    screen.blit(bulletImg, (x + 16, y + 10))


def isCollision(enemyX, enemyY, bulletX, bulletY): #define a function to check for collision
    distance = math.sqrt(math.pow(enemyX - bulletX, 2) + (math.pow(enemyY - bulletY, 2))) #Formula for distance
    if distance < 27:
        return True
    else:
        return False

def game_over_text(): #Show losing text
    over_text = font.render("A SOVIET SOLDIER KILLED YOU", True, black, white)
    screen.blit(over_text, (240, 240))
    time.sleep(5)

def you_won_text(): #Show winning text
    won_text = font.render("You won!", True, black, white)
    screen.blit(won_text, (240, 240))
    time.sleep(5)

# Game Loop
running = True
while running:

    # RGB = Red, Green, Blue
    screen.fill((0, 0, 0)) #Fill the screen with black
    # Background Image
    screen.blit(background, (0, 0)) #add background layer
    screen.blit(text1, (0, 450)) #Add the text
    screen.blit(text2, (0, 460))
    screen.blit(uranium, (240, 20)) #Add the uranium

    for event in pygame.event.get(): #if user presses x then quit
        if event.type == pygame.QUIT:
            running = False

        # if keystroke is pressed check whether its right or left
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                playerX_change = -1 #Change the value of playerX_change
            if event.key == pygame.K_RIGHT:
                playerX_change = 1 #Change the value of playerX_change
            if event.key == pygame.K_UP:
                playerY_change = -1 #Change the value of playerY_change
            if event.key == pygame.K_DOWN:
                playerY_change = 1 #Change the value of playerY_change
            if event.key == pygame.K_SPACE:
                if bullet_state == "ready":
                    # Get the current x cordinate of the player
                    bulletX = playerX
                    fire_bullet(bulletX, bulletY)

        if event.type == pygame.KEYUP: #If user leaves the key, then stop moving
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT or pygame.K_UP or event.key == pygame.K_DOWN:
                playerX_change = 0
                playerY_change = 0

    playerX += playerX_change #Add the value of playerX_change to players x coordinate
    playerY += playerY_change #Add the value of playerY_change to players y coordinate

    if playerX <= 0: #If player goes outside the boundary teleport them back in
        playerX = 0
    elif playerX >= 459:
        playerX = 459
    if playerY <= 0:
        playerY = 0
    elif playerY >= 459:
        playerY = 459

    # Enemy Movement
    for i in range(num_of_enemies):

        if enemyY[i] > 440:
            enemyImg = []
            enemyX = []
            enemyY = []
            enemyX_change = []
            enemyY_change = []
            num_of_enemies = 6

            for i in range(num_of_enemies): #Load number of enemies in a for loop
                enemyImg.append(pygame.image.load('enemy.png'))
                enemyX.append(random.randint(0, 480)) #Spawn enemy at random x coordinate
                enemyY.append(random.randint(50, 150)) #Spawn enemy at random y coordinate
                enemyX_change.append(1)
                enemyY_change.append(20)

        collision = isCollision(enemyX[i], enemyY[i], bulletX, bulletY) #Use the collision method
        if collision:
            bulletY = 480
            bullet_state = "ready"

            #Kill an enemy if it is shot
            del enemyX[i]
            del enemyY[i]
            del enemyX_change[i]
            del enemyY_change[i]
            num_of_enemies += -1
            break


        enemyX[i] += enemyX_change[i] #Defines a boundary for the enemies
        if enemyX[i] <= 0:
            enemyX_change[i] = 3
            enemyY[i] += enemyY_change[i]
        elif enemyX[i] >= 459:
            enemyX_change[i] = -3
            enemyY[i] += enemyY_change[i]

        if playerX >= enemyX[i]-20 and playerX <= enemyX[i]+20: #If a player comes near a soldier, then the soldier kills it
            if playerY <= enemyY[i]+20 and playerY >= enemyY[i]-20:
                game_over_text()
                print("You lost :(")
                quit()
            else:
                pass
        else:
            pass

        if playerX <= 250 and playerX >= 230: #If a player is near the uranium, say tht they won
            if playerY <= 30 and playerY >= 10:
                you_won_text()
                print("You won!")
                quit()
            else:
                pass
        else:
            pass



        enemy(enemyX[i], enemyY[i], i) #Teleport enemy to position

    if bulletY <= 0: #Fire bullets
        bulletY = 480
        bullet_state = "ready"

    if bullet_state == "fire":
        fire_bullet(bulletX, bulletY)
        bulletY -= bulletY_change

    player(playerX, playerY) #place player in the desired position
    pygame.display.flip() #update the screen
