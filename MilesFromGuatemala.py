###################################################################
########################                   ########################
########################  MILES            ########################
########################    FROM           ########################
########################      GUATEMALA    ########################
########################        by         ########################
########################          michael  ########################
########################            purdy  ########################
########################                   ########################
###################################################################

###################################################################
########################                   ########################
########################  IMPORT FUNCTIONS ########################
########################        &          ########################
########################  SET UP VARIABLES ########################
########################                   ########################
###################################################################
import pygame, sys, random
from pygame.locals import *
pygame.init()
global FPS
FPS = 30
fpsClock = pygame.time.Clock()
windowSurfaceObj = pygame.display.set_mode((500, 185))
pygame.display.set_caption('Miles from Guatemala!')
pygame.mouse.set_visible(False)
pygame.joystick.init()
joysticks = [pygame.joystick.Joystick(x) for x in range (pygame.joystick.get_count())]
global ENDscore
ENDscore = str
GameState = 1
#highscore = open('highscore.txt', 'r')
###################################################################
########################                   ########################
########################    GAME OVER      ########################
########################                   ########################
###################################################################
def GameOver(a):
  pygame.mixer.music.play(1, 46.30)
  pygame.key.set_repeat(0)
  GOfont = pygame.font.Font('freesansbold.ttf', 20)
  restartSurf = GOfont.render('RESTART', False, (237, 215, 29))
  restartX = 200
  restartY = 80
  menuSurf = GOfont.render('MENU', False, (237, 215, 29))
  menuX = 214
  menuY = 110
  exitSurf = GOfont.render('EXIT', False, (237, 215, 29))
  exitX = 221
  exitY = 140
  menuposition = 0
  goY = 1
  AnimCount = 1
  highscore = open('data/highscore.purdy', 'r')
  HighScore = highscore.read()
  while True:
    
    if AnimCount == 1:
      batsSurfaceObj = pygame.image.load('data/bat4.png')
      AnimCount += 1
    elif AnimCount == 2:
      batsSurfaceObj = pygame.image.load('data/bat3.png')
      AnimCount += 1
    elif AnimCount == 3:
      batsSurfaceObj = pygame.image.load('data/bat2.png')
      AnimCount += 1
    elif AnimCount == 4:
      batsSurfaceObj = pygame.image.load('data/bat1.png')
      AnimCount += 1
    elif AnimCount == 5:
      batsSurfaceObj = pygame.image.load('data/bat2.png')
      AnimCount += 1
    elif AnimCount == 6:
      batsSurfaceObj = pygame.image.load('data/bat3.png')
      AnimCount = 1
    batsSurfaceObj = pygame.transform.scale(batsSurfaceObj, (40, 20))

    FATEsurf = pygame.image.load('data/fate.png')
    GAMEOVERsurf = pygame.image.load('data/gameover.png')
    MILESsurf = pygame.image.load('data/miles.png')
    AUTHORsurf = pygame.image.load('data/author.png')
    SCOREfont = pygame.font.Font('freesansbold.ttf', 35)
    SCOREsurf = SCOREfont.render(a, False, (255, 20, 20))
    HIGHSCOREfont = pygame.font.Font('freesansbold.ttf', 35)
    HIGHSCOREsurf = HIGHSCOREfont.render(HighScore, False, (255, 20, 20))
    highscore.close()
    goY += 4
    windowSurfaceObj.fill((0, 0, 0))
    windowSurfaceObj.blit(FATEsurf, (0, -20 + goY))
    windowSurfaceObj.blit(MILESsurf, (0, -330 + goY))
    if goY <= 745:
      windowSurfaceObj.blit(AUTHORsurf, (0, -650 +goY))
    if goY >= 746:
      windowSurfaceObj.blit(AUTHORsurf, (0, 99))
    if goY >= 860:
      windowSurfaceObj.blit(SCOREsurf, (110, 112))
      windowSurfaceObj.blit(HIGHSCOREsurf, (110, 140))
    if goY >= 800:
      windowSurfaceObj.blit(GAMEOVERsurf, (0, 0))
    if goY >= 870:
      windowSurfaceObj.blit(restartSurf, (restartX, restartY))
      windowSurfaceObj.blit(menuSurf, (menuX, menuY))
      windowSurfaceObj.blit(exitSurf, (exitX, exitY))
    if goY >= 890:
      if goY <= 899:
        menuposition = 1
    if menuposition == 1:
      windowSurfaceObj.blit(batsSurfaceObj, (restartX - 60, restartY))
      windowSurfaceObj.blit(batsSurfaceObj, (restartX + 114, restartY))
    elif menuposition == 2:
      windowSurfaceObj.blit(batsSurfaceObj, (menuX -60, menuY))
      windowSurfaceObj.blit(batsSurfaceObj, (menuX +74, menuY))
    elif menuposition == 3:
      windowSurfaceObj.blit(batsSurfaceObj, (exitX -60, exitY))
      windowSurfaceObj.blit(batsSurfaceObj, (exitX +60, exitY))
      
    for event in pygame.event.get():
      if event.type == QUIT:
        pygame.quit()
        sys.exit()
      elif event.type == KEYUP:
        if event.key == K_ESCAPE:
          pygame.event.post(pygame.event.Event(QUIT))
        if event.key == K_UP:
          if menuposition == 2:
            menuposition = 1
          elif menuposition == 3:
            menuposition = 2
          elif menuposition == 1:
            menuposition = 3
        if event.key == K_DOWN:
          if menuposition == 1:
            menuposition = 2
          elif menuposition == 2:
            menuposition = 3
          elif menuposition == 3:
            menuposition = 1
        if event.key == K_RETURN:
          if goY <= 890:
            GameState = 2
            return GameState
          if menuposition == 1:
            GameState = 2
            return GameState
          if menuposition == 2:
            GameState = 1
            return GameState
          if menuposition == 3:
            pygame.event.post(pygame.event.Event(QUIT))    
    pygame.display.update()
    fpsClock.tick(30)

###################################################################
########################                   ########################
########################    MAIN GAME      ########################
########################                   ########################
###################################################################
def MainGame(a):
  pygame.mixer.music.load('data/bg.ogg')
  pygame.mixer.music.play(1,0)
  pygame.key.set_repeat(1, 1)
  GOanimX = 0
  GOanimY = 0
  DEAD = 0
  Agua = 0
  aguaX = 0
  scrollreset = 600
  lane = 'MID'
  HIT = 0
  milesY = int
  milesX = int
  AnimCount = 1
  passed_count = 10
  bgX = 0
  bgTX = 0
  bgTX2 = 600
  bgTopX = 1
  bgTopX2 = 600
  bgMidX = 1
  bgMidX2 = 600
  bgBotX = 1
  bgBotX2 = 600
  batsCollide = []
  bats = []
  TOPY = 53
  MIDY = 83
  BOTY = 135
  score = 0
  THROW = False
  for i in range(8):
    x=random.randrange(1000, 2000)
    y=random.randrange(1, 3)
    if y == 1:
      y = TOPY
    elif y == 2:
      y = MIDY
    elif y == 3:
      y = BOTY
    bats.append([x,y,2, 3])
    bgPic = pygame.image.load('data/bg.png').convert()
    bgTree = pygame.image.load('data/bgTrees.png')
    bgTree2 = pygame.image.load('data/bgTrees.png')
    bgTopLane = pygame.image.load('data/midlane.png')
    bgTopLane2 = pygame.image.load('data/midlane.png')
    bgMidLane = pygame.image.load('data/midlane.png')    
    bgMidLane = pygame.transform.scale(bgMidLane, (610, 36))
    bgMidLane2 = pygame.image.load('data/midlane.png')
    bgMidLane2 = pygame.transform.scale(bgMidLane2, (610, 36))
    bgBotLane = pygame.image.load('data/midlane.png')
    bgBotLane2 = pygame.image.load('data/midlane.png')
    milesSurfaceObj = pygame.image.load('data/run1.png')
    aguaIcon = pygame.image.load('data/agua.png')
    AGUAsurf = pygame.image.load('data/bigAGUA.png')
  while a == 0:

    bgX -= .2
    bgTX -= 2
    bgTX2 -= 2
    bgTopX -= 3
    bgTopX2 -= 3
    bgMidX -= 4
    bgMidX2 -= 4
    bgBotX -= 5
    bgBotX2 -= 5
    if bgTX2 < -scrollreset:
      bgTX2 = scrollreset
    if bgTX < -scrollreset:
      bgTX = scrollreset
    if bgTopX < -scrollreset:
      bgTopX = scrollreset
    if bgTopX2 < -scrollreset:
      bgTopX2 = scrollreset
    if bgMidX < -scrollreset:
      bgMidX = scrollreset
    if bgMidX2 < -scrollreset:
      bgMidX2 = scrollreset
    if bgBotX < -scrollreset:
      bgBotX = scrollreset
    if bgBotX2 < -scrollreset:
      bgBotX2 = scrollreset
    windowSurfaceObj.blit(bgPic, (bgX, -20))
    windowSurfaceObj.blit(bgTree, (bgTX, 0))
    windowSurfaceObj.blit(bgTree2, (bgTX2, 0))
    pygame.draw.rect(windowSurfaceObj, (0, 222, 0), (0, 60, 600, 75))
    windowSurfaceObj.blit(bgTopLane, (bgTopX, 70))
    windowSurfaceObj.blit(bgTopLane2, (bgTopX2, 70))
    pygame.draw.rect(windowSurfaceObj, (0, 222, 0), (0, 105, 600, 75))
    windowSurfaceObj.blit(bgMidLane, (bgMidX, 115))
    windowSurfaceObj.blit(bgMidLane2, (bgMidX2, 115))
    pygame.draw.rect(windowSurfaceObj, (0, 222, 0), (0, 150, 600, 75))
    windowSurfaceObj.blit(bgBotLane, (bgBotX, 170))
    windowSurfaceObj.blit(bgBotLane2, (bgBotX2, 170))

    #Animation#
    if AnimCount == 1:
      milesSurfaceObj = pygame.image.load("data/run4.png")
      batsSurfaceObj = pygame.image.load('data/bat4.png')
      AnimCount += 1
    elif AnimCount == 2:
      milesSurfaceObj = pygame.image.load('data/run3.png')
      batsSurfaceObj = pygame.image.load('data/bat3.png')
      AnimCount += 1
    elif AnimCount == 3:
      milesSurfaceObj = pygame.image.load('data/run2.png')
      batsSurfaceObj = pygame.image.load('data/bat2.png')
      AnimCount += 1
    elif AnimCount == 4:
      milesSurfaceObj = pygame.image.load('data/run1.png')
      batsSurfaceObj = pygame.image.load('data/bat1.png')
      AnimCount += 1
    elif AnimCount == 5:
      milesSurfaceObj = pygame.image.load('data/run2.png')
      batsSurfaceObj = pygame.image.load('data/bat2.png')
      AnimCount += 1
    elif AnimCount == 6:
      milesSurfaceObj = pygame.image.load('data/run3.png')
      batsSurfaceObj = pygame.image.load('data/bat3.png')
      AnimCount = 1
    ###Keyboard input
    ###Keyboard input
    ###Keyboard input
    ###Keyboard input
    ###Keyboard input
    ###Keyboard input
    if DEAD == 0:
      for event in pygame.event.get():
        if event.type == QUIT:
          pygame.quit()
          sys.exit()
        elif event.type == KEYDOWN:
          if event.key == K_SPACE:
            pygame.key.set_repeat(0,0)
            if Agua >= 1:
              THROW = True
          if event.key == K_ESCAPE:
            pygame.event.post(pygame.event.Event(QUIT))
          if event.key == K_UP:
            if lane != 'BOT':
              if event.key != K_DOWN:
                lane = 'TOP'
          if event.key == K_DOWN:
            if lane != 'TOP':
              lane = 'BOT'    
        if event.type == KEYUP:
          if event.key == K_UP:
            #if event.type == KEYDOWN:
              #if event.key != K_DOWN:
                lane = 'MID'
          if event.key == K_DOWN:
            lane = 'MID'
    if lane == 'TOP':
      milesX = 60
      milesY = 50
      milesSurfaceObj = pygame.transform.scale(milesSurfaceObj, (21, 36))
      milesRect = pygame.Rect(milesX, milesY-10, 10, 46)  
    if lane == 'MID':
      milesX = 40
      milesY = 80
      milesSurfaceObj = pygame.transform.scale(milesSurfaceObj, (28, 52))
      milesRect = pygame.Rect(milesX, milesY+5, 15, 40)
    if lane == 'BOT':
      milesX = 5
      milesY = 105 
      milesSurfaceObj = pygame.transform.scale(milesSurfaceObj, (70, 120))
      milesRect = pygame.Rect(milesX +10 , milesY+10, 10, 60)
    #Process bats#
    if DEAD == 0:
      for i in range(len(bats)):
        bats[i][0]-= passed_count/1.6
        if bats[i][1] == TOPY:
          batsSurfaceObj = pygame.transform.scale(batsSurfaceObj, (20, 10))
          bats[i][2] = 20
          bats[i][3] = 10
        elif bats[i][1] == MIDY:
          batsSurfaceObj = pygame.transform.scale(batsSurfaceObj, (40, 20))
          bats[i][2] = 40
          bats[i][3] = 20
        elif bats[i][1] == BOTY:
          batsSurfaceObj = pygame.transform.scale(batsSurfaceObj, (80, 40))
          bats[i][2] = 80
          bats[i][3] = 40
        if bats[i][0] < -80:
          score +=1
          x=random.randrange(500, 1500)
          bats[i][0]=x
          y=random.randrange(1,4)
          if y == 1:
            y = TOPY
          elif y == 2:
            y = MIDY 
          elif y == 3:
            y = BOTY
          bats[i][1]=y
          if passed_count < 40:
            passed_count += .2
        windowSurfaceObj.blit(batsSurfaceObj, bats[i])
    if DEAD == 0:
      windowSurfaceObj.blit(milesSurfaceObj, (milesX, milesY))
    if score % 50 == 0:
      Agua += 1
      score += 1
    milesCollide = milesRect
    #collison!!!
    #for i in range(8):
      #batRect = pygame.Rect(bats[i][0]+3,bats[i][1]+10,bats[i][2]-10,bats[i][3]-10)
      #batsCollide.append([batRect])
    batsCollide1 = pygame.Rect(bats[0][0]+3,bats[0][1]+10,bats[0][2]-15,bats[0][3]-10)
    batsCollide2 = pygame.Rect(bats[1][0]+3,bats[1][1]+10,bats[1][2]-15,bats[1][3]-10)
    batsCollide3 = pygame.Rect(bats[2][0]+3,bats[2][1]+10,bats[2][2]-15,bats[2][3]-10)
    batsCollide4 = pygame.Rect(bats[3][0]+3,bats[3][1]+10,bats[3][2]-15,bats[3][3]-10)
    batsCollide5 = pygame.Rect(bats[4][0]+3,bats[4][1]+10,bats[4][2]-15,bats[4][3]-10)
    batsCollide6 = pygame.Rect(bats[5][0]+3,bats[5][1]+10,bats[5][2]-15,bats[5][3]-10)
    batsCollide7 = pygame.Rect(bats[6][0]+3,bats[6][1]+10,bats[6][2]-15,bats[6][3]-10)
    batsCollide8 = pygame.Rect(bats[7][0]+3,bats[7][1]+10,bats[7][2]-15,bats[7][3]-10)
      #if milesCollide.colliderect(batsCollide[i]) == True:
        #HIT = 1
    if milesCollide.colliderect(batsCollide1) == True:
      HIT = 1
    elif milesCollide.colliderect(batsCollide2) == True:
      HIT = 1
    elif milesCollide.colliderect(batsCollide3) == True:
      HIT = 1
    elif milesCollide.colliderect(batsCollide4) == True:
      HIT = 1
    elif milesCollide.colliderect(batsCollide5) == True:
      HIT = 1  
    elif milesCollide.colliderect(batsCollide6) == True:
      HIT = 1
    elif milesCollide.colliderect(batsCollide7) == True:
      HIT = 1
    elif milesCollide.colliderect(batsCollide8) == True:
      HIT = 1
    pygame.draw.rect(windowSurfaceObj, (0, 0, 0), (450, 0, 50, 185))
    CurScore = str(score-1)
    curSCOREfont = pygame.font.Font('freesansbold.ttf', 20)
    smallfont = pygame.font.Font('freesansbold.ttf', 10)
    dodgedSurf = smallfont.render('Bats', False, (200, 10, 10))
    aguaSurf = smallfont.render('AGUA', False, (255, 255, 255))
    aguaSurf = pygame.transform.rotate(aguaSurf, 90)
    puraSurf = smallfont.render('PURA', False, (255, 255, 255))
    puraSurf = pygame.transform.rotate(puraSurf, 90)
    salvavidasSurf = smallfont.render('SALVAVIDAS', False, (255, 255, 255))
    salvavidasSurf = pygame.transform.rotate(salvavidasSurf, 90)
    SCOREsurf = curSCOREfont.render(CurScore, False, (255, 255, 255))
    windowSurfaceObj.blit(aguaSurf, (455, 110))
    windowSurfaceObj.blit(puraSurf, (455, 73))
    windowSurfaceObj.blit(salvavidasSurf, (455, 2))
    windowSurfaceObj.blit(dodgedSurf, (467, 140))
    windowSurfaceObj.blit(SCOREsurf, (455, 160))  
    if Agua >= 1:
      windowSurfaceObj.blit(aguaIcon, (475, 5))
    if Agua >= 2:
      windowSurfaceObj.blit(aguaIcon, (475, 27))
    if Agua >= 3:
      windowSurfaceObj.blit(aguaIcon, (475, 48))
    if Agua >= 4:
      windowSurfaceObj.blit(aguaIcon, (475, 69))
    if Agua >= 5:
      windowSurfaceObj.blit(aguaIcon, (475, 90))
    if Agua >= 6:
      windowSurfaceObj.blit(aguaIcon, (475, 111))

    if HIT == 1:
      pygame.mixer.music.fadeout(750)
      DEAD = 1
      AnimCount = 0
      if GOanimX <= 40:
        GOanimX += 3
        windowSurfaceObj.blit(milesSurfaceObj, (milesX, milesY - GOanimX))
      elif GOanimX >= 40:
        GOanimY += 5
        windowSurfaceObj.blit(milesSurfaceObj, (milesX, milesY - GOanimX + GOanimY))
      if GOanimY >= 180:
        score -= 1
        highscore = open('data/highscore.purdy', 'r')
        HighScore = highscore.read()
        CurHighScore = int(HighScore)
        pygame.mixer.music.load('data/lose.ogg')
        if score >= CurHighScore:
          pygame.mixer.music.load('data/win.ogg')
          highscore = open('data/highscore.purdy', 'w')
          highscore.write(str(score))
          pygame.mixer.music.load('data/win.ogg')
          highscore.close()
        highscore.close()
        score = str(score)
        return score

    if THROW == True:
      if HIT == 0:
        if aguaX <= 600:
          aguaCollide = pygame.Rect(aguaX, 0, 85, 79)
          windowSurfaceObj.blit(AGUAsurf, (aguaX, 0))
          aguaX += 40
          for i in range(len(bats)):
            if aguaX + 40 >= bats[i][0]:
              bats[i][0] = -90
              score -= 1
        if aguaX >= 600:
          THROW = False
          Agua -= 1
          aguaX = -0
    pygame.display.update()      
    fpsClock.tick(FPS)


###################################################################
########################                   ########################
########################    DIRECTIONS     ########################
########################                   ########################
###################################################################
def Directions(a):
  pygame.mixer.music.load('data/bg.ogg')
  pygame.mixer.music.play(1,0)
  pygame.key.set_repeat(0)
  directtime = 0
  GOanimX = 0
  GOanimY = 0
  DEAD = 0
  Agua = 1
  aguaX = 0
  scrollreset = 600
  lane = 'MID'
  HIT = 0
  milesY = int
  milesX = int
  AnimCount = 1
  bgX = 0
  bgTX = 0
  bgTX2 = 600
  bgTopX = 1
  bgTopX2 = 600
  bgMidX = 1
  bgMidX2 = 600
  bgBotX = 1
  bgBotX2 = 600
  TOPY = 53
  MIDY = 83
  BOTY = 135
  score = 0
  THROW = False

  directions1 = pygame.image.load('data/directions/directions1.png')
  directions2 = pygame.image.load('data/directions/directions2.png') 
  directions3 = pygame.image.load('data/directions/directions3.png') 
  directions4 = pygame.image.load('data/directions/directions4.png')  
  directions5 = pygame.image.load('data/directions/directions5.png')  
  directions6 = pygame.image.load('data/directions/directions6.png')  
  directions7 = pygame.image.load('data/directions/directions7.png')  
  bgPic = pygame.image.load('data/bg.png').convert()
  bgTree = pygame.image.load('data/bgTrees.png')
  bgTree2 = pygame.image.load('data/bgTrees.png')
  bgTopLane = pygame.image.load('data/midlane.png')
  bgTopLane2 = pygame.image.load('data/midlane.png')
  bgMidLane = pygame.image.load('data/midlane.png')    
  bgMidLane = pygame.transform.scale(bgMidLane, (610, 35))
  bgMidLane2 = pygame.image.load('data/midlane.png')
  bgMidLane2 = pygame.transform.scale(bgMidLane2, (610, 35))
  bgBotLane = pygame.image.load('data/midlane.png')
  bgBotLane2 = pygame.image.load('data/midlane.png')
  milesSurfaceObj = pygame.image.load('data/run1.png')
  aguaIcon = pygame.image.load('data/agua.png')
  AGUAsurf = pygame.image.load('data/bigAGUA.png')
  returnSurf = pygame.image.load('data/directions/return.png')

  while True:
    directtime += 5
    bgX -= .2
    bgTX -= 2
    bgTX2 -= 2
    bgTopX -= 3
    bgTopX2 -= 3
    bgMidX -= 4
    bgMidX2 -= 4
    bgBotX -= 5
    bgBotX2 -= 5
    if bgTX2 < -scrollreset:
      bgTX2 = scrollreset
    if bgTX < -scrollreset:
      bgTX = scrollreset
    if bgTopX < -scrollreset:
      bgTopX = scrollreset
    if bgTopX2 < -scrollreset:
      bgTopX2 = scrollreset
    if bgMidX < -scrollreset:
      bgMidX = scrollreset
    if bgMidX2 < -scrollreset:
      bgMidX2 = scrollreset
    if bgBotX < -scrollreset:
      bgBotX = scrollreset
    if bgBotX2 < -scrollreset:
      bgBotX2 = scrollreset
    windowSurfaceObj.blit(bgPic, (bgX, -20))
    windowSurfaceObj.blit(bgTree, (bgTX, 0))
    windowSurfaceObj.blit(bgTree2, (bgTX2, 0))
    pygame.draw.rect(windowSurfaceObj, (0, 222, 0), (0, 60, 600, 75))
    windowSurfaceObj.blit(bgTopLane, (bgTopX, 70))
    windowSurfaceObj.blit(bgTopLane2, (bgTopX2, 70))
    pygame.draw.rect(windowSurfaceObj, (0, 222, 0), (0, 105, 600, 75))
    windowSurfaceObj.blit(bgMidLane, (bgMidX, 115))
    windowSurfaceObj.blit(bgMidLane2, (bgMidX2, 115))
    pygame.draw.rect(windowSurfaceObj, (0, 222, 0), (0, 150, 600, 75))
    windowSurfaceObj.blit(bgBotLane, (bgBotX, 170))
    windowSurfaceObj.blit(bgBotLane2, (bgBotX2, 170))
        
#####Animation#
    if AnimCount == 1:
      milesSurfaceObj = pygame.image.load("data/run4.png")
      batsSurfaceObj = pygame.image.load('data/bat4.png')
      AnimCount += 1
    elif AnimCount == 2:
      milesSurfaceObj = pygame.image.load('data/run3.png')
      batsSurfaceObj = pygame.image.load('data/bat3.png')
      AnimCount += 1
    elif AnimCount == 3:
      milesSurfaceObj = pygame.image.load('data/run2.png')
      batsSurfaceObj = pygame.image.load('data/bat2.png')
      AnimCount += 1
    elif AnimCount == 4:
      milesSurfaceObj = pygame.image.load('data/run1.png')
      batsSurfaceObj = pygame.image.load('data/bat1.png')
      AnimCount += 1
    elif AnimCount == 5:
      milesSurfaceObj = pygame.image.load('data/run2.png')
      batsSurfaceObj = pygame.image.load('data/bat2.png')
      AnimCount += 1
    elif AnimCount == 6:
      milesSurfaceObj = pygame.image.load('data/run3.png')
      batsSurfaceObj = pygame.image.load('data/bat3.png')
      AnimCount = 1
#####
    for event in pygame.event.get():
      if event.type == KEYDOWN:
        if event.key == K_RETURN:
          GameState = 1
          return GameState
    
    if lane == 'TOP':
      milesX = 60
      milesY = 50
      milesSurfaceObj = pygame.transform.scale(milesSurfaceObj, (21, 36))
      milesRect = pygame.Rect(milesX, milesY-10, 10, 46)  
    if lane == 'MID':
      milesX = 40
      milesY = 80
      milesSurfaceObj = pygame.transform.scale(milesSurfaceObj, (28, 52))
      milesRect = pygame.Rect(milesX, milesY+5, 15, 40)
    if lane == 'BOT':
      milesX = 5
      milesY = 105 
      milesSurfaceObj = pygame.transform.scale(milesSurfaceObj, (70, 120))
      milesRect = pygame.Rect(milesX +10 , milesY+10, 10, 60)
    exbat1 = pygame.transform.scale(batsSurfaceObj, (20, 10))
    exbat2 = pygame.transform.scale(batsSurfaceObj, (40, 20))
    exbat3 = pygame.transform.scale(batsSurfaceObj, (80, 40))
    exbat4 = pygame.transform.scale(batsSurfaceObj, (20, 10))
    exbat5 = pygame.transform.scale(batsSurfaceObj, (40, 20))
    exbat6 = pygame.transform.scale(batsSurfaceObj, (80, 40))
    exbat7 = pygame.transform.scale(batsSurfaceObj, (20, 10))
    exbat8 = pygame.transform.scale(batsSurfaceObj, (40, 20))
    exbat9 = pygame.transform.scale(batsSurfaceObj, (80, 40))
    exbat10 = pygame.transform.scale(batsSurfaceObj, (40, 20))
    if directtime > 1:
      windowSurfaceObj.blit(milesSurfaceObj, (milesX, milesY))
      windowSurfaceObj.blit(exbat1, (700 - directtime, TOPY))
      windowSurfaceObj.blit(exbat2, (750  - directtime, MIDY))
      windowSurfaceObj.blit(exbat3, (800 - directtime, BOTY))
      windowSurfaceObj.blit(exbat4, (1000 - directtime, TOPY))
      windowSurfaceObj.blit(exbat5, (1080 - directtime, MIDY))
      windowSurfaceObj.blit(exbat6, (1160 - directtime, BOTY))
      windowSurfaceObj.blit(exbat7, (2000 - directtime, TOPY))
      windowSurfaceObj.blit(exbat8, (2000 - directtime, MIDY))
      windowSurfaceObj.blit(exbat9, (2000 - directtime, BOTY))
    if directtime == 195:
      windowSurfaceObj.blit(directions1, (0, 0))
    if directtime == 200:
      pygame.time.delay(3000)
    if directtime == 405:
      windowSurfaceObj.blit(directions2, (0, 0))
    if directtime == 410:
      pygame.time.delay(3000)
    if directtime == 655:
      windowSurfaceObj.blit(directions3, (0, 0))
    if directtime == 660:
      pygame.time.delay(3000)
    if directtime >= 670:
      lane = 'TOP' 
    ##score
    if directtime == 750:
      score += 1
    elif directtime == 800:
      score += 1
    elif directtime == 850:
      score += 1
    elif directtime == 1070:
      score += 1
    elif directtime == 1150:
      score += 1
    elif directtime == 1210:
      score += 1
    if directtime == 725:
      windowSurfaceObj.blit(directions4, (0, 0))
    if directtime == 730:
      pygame.time.delay(3000)
    if directtime >= 740:
      lane = 'MID'
    if directtime == 865:
      windowSurfaceObj.blit(directions5, (0, 0))
    if directtime == 870:
      pygame.time.delay(3000)  
    if directtime >= 880:
      lane = 'BOT'
    if directtime == 1065:
      windowSurfaceObj.blit(directions6, (0, 0))
    if directtime == 1070:
      pygame.time.delay(3000)
    if directtime >= 1070:
      lane = 'MID'
    if directtime == 1595:
      windowSurfaceObj.blit(directions7, (0, 0))
    if directtime == 1600:
      pygame.time.delay(7000)
    if directtime >= 1850:
      if Agua == 1:
        if aguaX <= 600:
          windowSurfaceObj.blit(AGUAsurf, (aguaX, 0))
          aguaX += 40
          if aguaX >= 100:
            directtime = 2500
          if aguaX >= 600:
            aguaX = 40
            Agua -= 1
    if directtime >= 2550:
      for event in pygame.event.get():
        if event.key == K_RETURN:
          GameState = 2
          return GameState
      windowSurfaceObj.blit(returnSurf, (-50, 0))
  

#####HUD####    
    pygame.draw.rect(windowSurfaceObj, (0, 0, 0), (450, 0, 50, 185))
    CurScore = str(score)
    curSCOREfont = pygame.font.Font('freesansbold.ttf', 20)
    smallfont = pygame.font.Font('freesansbold.ttf', 10)
    dodgedSurf = smallfont.render('Bats', False, (200, 10, 10))
    aguaSurf = smallfont.render('AGUA', False, (255, 255, 255))
    aguaSurf = pygame.transform.rotate(aguaSurf, 90)
    puraSurf = smallfont.render('PURA', False, (255, 255, 255))
    puraSurf = pygame.transform.rotate(puraSurf, 90)
    salvavidasSurf = smallfont.render('SALVAVIDAS', False, (255, 255, 255))
    salvavidasSurf = pygame.transform.rotate(salvavidasSurf, 90)
    SCOREsurf = curSCOREfont.render(CurScore, False, (255, 255, 255))
    windowSurfaceObj.blit(aguaSurf, (455, 110))
    windowSurfaceObj.blit(puraSurf, (455, 73))
    windowSurfaceObj.blit(salvavidasSurf, (455, 2))
    windowSurfaceObj.blit(dodgedSurf, (467, 140))
    windowSurfaceObj.blit(SCOREsurf, (455, 160))  
    if Agua == 1:
      windowSurfaceObj.blit(aguaIcon, (475, 5))

    pygame.display.update()      
    fpsClock.tick(FPS)


###################################################################
########################                   ########################
########################   START SCREEN    ########################
########################                   ########################
###################################################################


def StartScreen(a):
  pygame.mixer.music.load('data/intro.ogg')
  pygame.key.set_repeat(0)
  charX = -85
  charX2 = -320
  AnimCount = 1
  menuposition = 0
  introY2 = 1
  introY = 1
  MFGw = 500
  MFGh = 185
  skip = False
  OPERATIONMARTILLOsurf = pygame.image.load('data/OperationMartillo.png')
  #MILESFROMGUATsurf = pygame.image.load('guatemala.png')
  INTROsurf = pygame.image.load('data/intro.png')
  STARTsurf = pygame.image.load('data/startscreen.png')
  STARTMENUsurf = pygame.image.load('data/startscreenmenu.png')
  while a == 0:
    #OPERATIONMARTILLOsurf = pygame.image.load('OperationMartillo.png')
    MILESFROMGUATsurf = pygame.image.load('data/guatemala.png')
    #INTROsurf = pygame.image.load('intro.png')
    #STARTsurf = pygame.image.load('startscreen.png')
    #STARTMENUsurf = pygame.image.load('startscreenmenu.png')
    if introY <= 300:
      introY +=1
    introY += .5
    windowSurfaceObj.fill((0, 0, 0))
    if introY >= 0:
      if introY <= 75:
        pygame.mixer.music.play(1, 26.25)
        windowSurfaceObj.blit(OPERATIONMARTILLOsurf, (0,0))
    if introY >= 130:
      if introY <=230:
        windowSurfaceObj.blit(MILESFROMGUATsurf, (0,0))
    if introY >= 350:
      windowSurfaceObj.blit(INTROsurf, (0, 565-introY))


    if skip == True:
      introY += 1000
    if introY >= 1000:
      skip = True
      introY2 += 1
      if introY2 <= 60:
        menuposition = 1
        
      if MFGw >= 300:
        MFGw -= 8
        MFGh -= 4
        MILESFROMGUATsurf = pygame.transform.scale(MILESFROMGUATsurf, (MFGw, MFGh))
        windowSurfaceObj.blit(MILESFROMGUATsurf, (0, 0))
      MILESFROMGUATsurf = pygame.transform.scale(MILESFROMGUATsurf, (MFGw, MFGh))
      windowSurfaceObj.blit(MILESFROMGUATsurf, (0, 0))
      if introY2 >= 40:
        windowSurfaceObj.blit(STARTMENUsurf, (0, 0))
      if introY2 >= 60:
        if charX >= 670:
          charX = -85
          charX2 = -320
        if charX <= 670:
          charX += 3
          charX2 += 4
        if menuposition == 1:
          pygame.draw.line(windowSurfaceObj, (237, 215, 29), (430, 75), (487, 75) , 2)
        elif menuposition == 2:
          pygame.draw.line(windowSurfaceObj, (237, 215, 29), (380, 125), (487, 125) , 2)
        elif menuposition == 3:
          pygame.draw.line(windowSurfaceObj, (237, 215, 29), (450, 172), (487, 172) , 2)
      if AnimCount == 1:
        milesSurfaceObj = pygame.image.load("data/run4.png")
        batsSurfaceObj = pygame.image.load('data/bat4.png')
        AnimCount += 1
      elif AnimCount == 2:
        milesSurfaceObj = pygame.image.load('data/run3.png')
        batsSurfaceObj = pygame.image.load('data/bat3.png')
        AnimCount += 1
      elif AnimCount == 3:
        milesSurfaceObj = pygame.image.load('data/run2.png')
        batsSurfaceObj = pygame.image.load('data/bat2.png')
        AnimCount += 1
      elif AnimCount == 4:
        milesSurfaceObj = pygame.image.load('data/run1.png')
        batsSurfaceObj = pygame.image.load('data/bat1.png')
        AnimCount += 1
      elif AnimCount == 5:
        milesSurfaceObj = pygame.image.load('data/run2.png')
        batsSurfaceObj = pygame.image.load('data/bat2.png')
        AnimCount += 1
      elif AnimCount == 6:
        milesSurfaceObj = pygame.image.load('data/run3.png')
        batsSurfaceObj = pygame.image.load('data/bat3.png')
        AnimCount = 1
      pygame.transform.flip(batsSurfaceObj, True, False)
      
      milesSurfaceObj = pygame.transform.scale(milesSurfaceObj, (70, 120))
      batsSurfaceObj = pygame.transform.scale(batsSurfaceObj, (80, 40))
      windowSurfaceObj.blit(milesSurfaceObj, (charX, 60))
      windowSurfaceObj.blit(batsSurfaceObj, (charX2, 100))
    

    for event in pygame.event.get():
      if event.type == QUIT:
        pygame.quit()
        sys.exit()
      elif event.type == KEYUP:
        if event.key == K_f:
          pygame.display.toggle_fullscreen()
        if event.key == K_UP:
          if menuposition == 1:
            menuposition = 3
          elif menuposition == 2:
            menuposition = 1
          elif menuposition == 3:
            menuposition = 2
        if event.key == K_DOWN:
          if menuposition == 1:
            menuposition = 2
          elif menuposition == 2:
            menuposition = 3
          elif menuposition == 3:
            menuposition = 1
        if event.key == K_RETURN:
          introY += 1000
          if skip == True:
            if menuposition == 1:
              GameState = 2
              return GameState
            if menuposition == 2:
              GameState = 1.5
              return GameState
            if menuposition == 3:
              pygame.event.post(pygame.event.Event(QUIT))
            #skip = True
        if event.key == K_ESCAPE:
          pygame.event.post(pygame.event.Event(QUIT))
    pygame.display.update()
    fpsClock.tick(FPS)

###################################################################
########################                   ########################
########################    GAME LOOP      ########################
########################                   ########################
###################################################################
while True:
  if GameState == 1:
    GameState = StartScreen(0)
  elif GameState == 1.5:
    GameState = Directions(0)
  elif GameState == 2:
    ENDscore = MainGame(0)
    GameState += 1
  if GameState == 3:
    GameState = GameOver(ENDscore)
