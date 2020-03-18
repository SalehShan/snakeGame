# Developed By Mayur Pawar
# ENjoy the game with the root control ! xD
# PYTHON Programmer
import pygame
import random
pygame.init()

white=(255,255,255)
red=(250,0,0)
black=(0,0,0)
blue=(0,0,255)
orange = (225,75,22)

global fps 
screenWidth = 700
screenHeight = 450

# Creating Window
gameWindow = pygame.display.set_mode((screenWidth,screenHeight))
pygame.display.set_caption("Pawars Production")
pygame.display.update()




clock = pygame.time.Clock()
font = pygame.font.SysFont(None, 40, bold=True, italic=False)

def textScreen(text, color, x, y):
    screenText = font.render(text,True, color)
    gameWindow.blit(screenText, (x, y))

def plotSnake(gameWindow, color, snkList, snakeSize):
    for x,y in snkList:
        pygame.draw.rect(gameWindow, color,[x,y,snakeSize,snakeSize])
def welScreen():
    exitGame = False
    fps = 100
    while not exitGame:
        gameWindow.fill(orange)
        textScreen("Welcome to Snake Game",black,150,180)
        textScreen("Press Space for Start Game",black,130,220)


        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exitGame = True

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    gameLoop()

        pygame.display.update()
        clock.tick(fps)


# Creating Game loop
def gameLoop():
    # Game specific Variable
    exitGame = False
    gameOver = False
    snake_X = 245
    snake_Y = 55
    snakeSize = 10
    valocity_X = 0
    valocity_Y = 0
    init_Valocity = 1
    food_X = random.randint(20,screenWidth-20)
    food_Y = random.randint(20,screenHeight-20)
    foodSize = 10
    score = 0
    snkList = []
    snkLenght = 1
    highScore = 30
    fps = 100

    with open("highScore.txt", "r") as f:
        hScore = f.read()
        

    while not exitGame:
        if gameOver:
            gameWindow.fill(white)
            textScreen("Final Score: "+str(score) + "    High Score: "+str(hScore),blue, 120, 150)
            textScreen("Game Over! press 'Enter' key to continue", red, 45, 200)
            with open("highScore.txt","w") as f:
                f.write(str(hScore))


            for event in pygame.event.get():
                
                if event.type == pygame.QUIT:
                    exitGame = True

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        gameLoop()
            
        else:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exitGame = True

                # Snake Moving Control
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RIGHT:
                        valocity_X = init_Valocity
                        valocity_Y = 0
                        # snake_X = snake_X + 10
                    if event.key == pygame.K_LEFT:
                        valocity_X = - init_Valocity
                        valocity_Y = 0
                        # snake_X = snake_X - 10
                        # print("Left pressed")
                    if event.key == pygame.K_DOWN:
                        valocity_Y = init_Valocity
                        valocity_X = 0
                        # snake_Y = snake_Y + 10
                        # print(" Down pressed")
                    if event.key == pygame.K_UP:
                        valocity_Y = - init_Valocity
                        valocity_X = 0
                        # snake_Y = snake_Y - 10
                        # print(" Up pressed")

                    #cheat code for increase score
                    if event.key == pygame.K_a:
                        score += 7
                    
            snake_X = snake_X + valocity_X
            snake_Y = snake_Y + valocity_Y

            gameWindow.fill(white)

            # Eating a food
            if abs(snake_X - food_X) < 10 and abs(snake_Y - food_Y) < 10:
                score += 1
                # print("Score=",score)
                
                food_X = random.randint(20,screenWidth/2)
                food_Y = random.randint(20,screenHeight/2)
                snkLenght += 5
                if score > int(hScore):
                    hScore = score


            head = []
            head.append(snake_X)
            head.append(snake_Y)
            snkList.append(head)

            if len(snkList)>snkLenght:
                del snkList[0]
            
            if  snake_X < 0 or snake_X > screenWidth or snake_Y < 0 or snake_Y > screenHeight:
                gameOver = True
            
            if head in snkList[:-1]:
                gameOver = True

            pygame.draw.rect(gameWindow, red, [food_X,food_Y,foodSize,foodSize])
            pygame.draw.rect(gameWindow, black,[snake_X,snake_Y,snakeSize,snakeSize])
            plotSnake(gameWindow,black, snkList, snakeSize)
            textScreen("Score: "+str(score)+ "      High Score: "+str(hScore),blue, 5, 5)

        pygame.display.update()
        clock.tick(fps)

    pygame.quit()
    quit()


welScreen()