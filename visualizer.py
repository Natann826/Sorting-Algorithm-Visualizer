import pygame
import random as r

from sorts import bubbleSort, insertionSort, selectionSort

pygame.init()

def plot(orig, data): # data is a generator object
    window_height = 500
    win = pygame.display.set_mode((1000, window_height))
    length = 200 / len(orig)
    width = 1

    blockList = []
    x = 10
    for number in orig:
        blockList.append(pygame.Rect(x, window_height - number * length, width, number * length))
        x += width + 1

    colors = [((r.randint(100, 255)), (r.randint(100, 255)), (r.randint(100, 255))) for i in range(len(orig))]

    for current in data:
        pygame.time.delay(20)

        win.fill((0, 0, 0)) 

        for block in range(len(blockList)):
            pygame.draw.rect(win,colors[block], blockList[block])

        pygame.display.update()

        for i in range(len(blockList)):
            blockList[i][3] = current[i] * length
            blockList[i][1] = window_height - blockList[i][3]

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
    
    for block in blockList:
            pygame.draw.rect(win, (255, 255, 255), block)

    pygame.display.update()
    pygame.time.delay(200)


randomList = [i for i in range(450)]
r.shuffle(randomList)

plot(randomList, insertionSort(randomList))
