import pygame,sys
if __name__=="__main__":
    pygame.init()
    pygame.font.init()
    pygame.mixer.init()
#class for characters
class Character:
    def __init__(self,left,right,stand,weapon):
        self.left=left
        self.right=right
        self.stand=stand
        self.stand=pygame.transform.scale(self.stand,(125,125))
        self.state=stand
        self.weapon=weapon
        self.weapon=pygame.transform.scale(self.weapon,(90,90))
        self.weaponrect=self.weapon.get_rect()
        for i in range(6):
            self.right[i]=pygame.transform.scale(self.right[i],(125,125))
            self.left[i]=pygame.transform.scale(self.left[i],(125,125))

myfont=pygame.font.SysFont('Comic Sans MS',200)
myfonto=pygame.font.SysFont('Comic Sans MS',100)
myfontl=pygame.font.SysFont('Comic Sans MS',30)
size = width, height = 1800, 1000
black = (0, 0, 0)

screen = pygame.display.set_mode(size)
#Fonts
Menu=myfont.render("MENU",False,(0,255,0))
Start=myfonto.render("START",False,(0,255,0))
Quit=myfonto.render("QUIT",False,(0,255,0))
#Menu background
menubg=pygame.image.load("menu.png")
menubg=pygame.transform.scale(menubg,(1800,1000))
#Captain stationary is caps

#Road
road=pygame.image.load("road.png")
road=pygame.transform.scale(road,(1800,125))
roadrect=road.get_rect()

#Music Loading
music=pygame.mixer.music.load("music.mp3")
pygame.mixer.music.play(-1)

#Loading left and right arrays of images
capr=[pygame.image.load("cap/capr1.png"),pygame.image.load("cap/capr2.png"),pygame.image.load("cap/capr3.png"),pygame.image.load("cap/capr4.png"),pygame.image.load("cap/capr5.png"),pygame.image.load("cap/capr6.png")]
capl=[pygame.image.load("cap/capl1.png"),pygame.image.load("cap/capl2.png"),pygame.image.load("cap/capl3.png"),pygame.image.load("cap/capl4.png"),pygame.image.load("cap/capl5.png"),pygame.image.load("cap/capl6.png")]
hawkl=[pygame.image.load("hawkeye/hawkl1.png"),pygame.image.load("hawkeye/hawkl2.png"),pygame.image.load("hawkeye/hawkl3.png"),pygame.image.load("hawkeye/hawkl4.png"),pygame.image.load("hawkeye/hawkl5.png"),pygame.image.load("hawkeye/hawkl6.png")]
hawkr=[pygame.image.load("hawkeye/hawkr1.png"),pygame.image.load("hawkeye/hawkr2.png"),pygame.image.load("hawkeye/hawkr3.png"),pygame.image.load("hawkeye/hawkr4.png"),pygame.image.load("hawkeye/hawkr5.png"),pygame.image.load("hawkeye/hawkr6.png")]
ironr=[pygame.image.load("ironman/ironr1.png"),pygame.image.load("ironman/ironr2.png"),pygame.image.load("ironman/ironr3.png"),pygame.image.load("ironman/ironr4.png"),pygame.image.load("ironman/ironr5.png"),pygame.image.load("ironman/ironr6.png")]
ironl=[pygame.image.load("ironman/ironl1.png"),pygame.image.load("ironman/ironl2.png"),pygame.image.load("ironman/ironl3.png"),pygame.image.load("ironman/ironl4.png"),pygame.image.load("ironman/ironl5.png"),pygame.image.load("ironman/ironl6.png")]
spiderl=[pygame.image.load("spiderman/spiderl1.png"),pygame.image.load("spiderman/spiderl2.png"),pygame.image.load("spiderman/spiderl3.png"),pygame.image.load("spiderman/spiderl4.png"),pygame.image.load("spiderman/spiderl5.png"),pygame.image.load("spiderman/spiderl6.png")]
spiderr=[pygame.image.load("spiderman/spiderr1.png"),pygame.image.load("spiderman/spiderr2.png"),pygame.image.load("spiderman/spiderr3.png"),pygame.image.load("spiderman/spiderr4.png"),pygame.image.load("spiderman/spiderr5.png"),pygame.image.load("spiderman/spiderr6.png")]
for i in range(6):
    capr[i]=pygame.transform.scale(capr[i],(125,125))
    capl[i]=pygame.transform.scale(capl[i],(125,125))
#Tank display
tank=pygame.image.load("tank.png")
tank=pygame.transform.scale(tank,(125,125))
#Characters creation
spiderman=Character(spiderl,spiderr,pygame.image.load("spiderman/spider.png"),pygame.image.load("spiderman/web.png"))
ironman=Character(ironl,ironr,pygame.image.load("ironman/iron.png"),pygame.image.load("ironman/laser.png"))
hawkeye=Character(hawkl,hawkr,pygame.image.load("hawkeye/hawk.png"),pygame.image.load("hawkeye/arrow.png"))
cap=Character(capl,capr,pygame.image.load("cap/captain.png"),pygame.image.load("cap/shield.png"))
chars=[spiderman,ironman,hawkeye,cap]#list of characters
k=0#whether shield has to be fired or not
x=0#x coordinate of character
y=0#y coordinate of character
l=0#counter for sprite array
#LIFE OF TANKS IS t
t=[1,1,1,1,1,1,1,1]
s=[]#coordinate of bullets
m=[]#whether bullets have to be fired or not
bulletimg=pygame.image.load("bullet.png")#bullet img
bulletimg=pygame.transform.scale(bulletimg,(50,50))
for i in range(8):
    s.append([1800-125,40 + i*125])
    m.append(False)
xm=770#x coordinate of selection rectangle in menu
ym=430#y coordinate of selection rect
rectl=270#rectange length
rectb=120#rectange breadth
lives=3#lives
count=10#no of times a sprite is displayed
level=1#Levels
levelc=1#If level has to be displayed or not
speed=10# speed at which bullets come

pygame.display.set_caption("Bullet Tanks")
#Start Of the game loop
while 1:
    #Start of menu
    while 1:
        for event in pygame.event.get():
            if event.type == pygame.QUIT: sys.exit()
        keys=pygame.key.get_pressed()
        if keys[pygame.K_DOWN] and ym!=430+rectb:
            ym+=rectb
        if keys[pygame.K_UP] and ym!=430:
            ym-=rectb
        if keys[pygame.K_RETURN]:
            if ym==430:
                break
            elif ym==430+rectb:
                sys.exit()
        screen.blit(menubg,(0,0))
        screen.blit(Menu,(700,200))
        pygame.draw.lines(screen,(255,0,0),True,[(xm,ym),(xm+rectl,ym),(xm+rectl,ym+rectb),(xm,ym+rectb)],10)
        screen.blit(Start,(800,450))
        screen.blit(Quit,(830,550))
        pygame.display.update()
    #image loading for buttons
    rightb=pygame.image.load("right.jpg")
    leftb=pygame.image.load("left.png")
    leftb=pygame.transform.scale(leftb,(50,50))
    rightb=pygame.transform.scale(rightb,(50,50))
    submit=pygame.image.load("submit.png")
    submit=pygame.transform.scale(submit,(200,50))
#Character Choosing
    r=0
    while 1:
        for event in pygame.event.get():
            if event.type == pygame.QUIT: sys.exit()
        pygame.mouse.get_pressed()
        if event.type==pygame.MOUSEBUTTONDOWN:
            if pygame.mouse.get_pos()[0] > 1250 and pygame.mouse.get_pos()[0] < 1300 and pygame.mouse.get_pos()[1] > 500 and pygame.mouse.get_pos()[1] < 550 and r<3:
                r+=1
            if pygame.mouse.get_pos()[0] > 350 and pygame.mouse.get_pos()[0] < 400 and pygame.mouse.get_pos()[1] > 500 and pygame.mouse.get_pos()[1] < 550:
                if r>0:
                    r-=1
            if pygame.mouse.get_pos()[0] > 750 and pygame.mouse.get_pos()[0] < 950 and pygame.mouse.get_pos()[1] > 800 and pygame.mouse.get_pos()[1] < 850:
                break
        chars[r].stand=pygame.transform.scale(chars[r].stand,(400,400))
        screen.blit(menubg,(0,0))
        screen.blit(rightb,(1250,500))
        screen.blit(leftb,(350,500))
        screen.blit(submit,(750,800))
        screen.blit(chars[r].stand,(650,300))
        pygame.display.update()
    #Reinitialising all variables
    k=0
    x=0
    y=0
    l=0
    t=[1,1,1,1,1,1,1,1]
    s=[]
    m=[]
    for i in range(8):
        s.append([1800-125,40 + i*125])
        m.append(False)
    p=1
    lives=3
    levelc=1
    count=10
    level=1
    speed=5
    char=chars[r]
    char.stand=pygame.transform.scale(char.stand,(125,125))
    char.state=char.stand
#main game
    while 1:
        for event in pygame.event.get():
            if event.type == pygame.QUIT: sys.exit()

        levels=myfont.render("Level:"+str(level),False,(255,0,0))

        vx=0
        vy=0
        keys=pygame.key.get_pressed()
#Controls of the game
        if event.type==pygame.KEYDOWN:
            if event.key == pygame.K_UP and y>0:
                y-=10
                vy=-10
                char.state=char.stand
                l=0
            if event.key == pygame.K_DOWN and (y+125)<height:
                y+=10
                vy=10
                char.state=char.stand
                l=0
            if event.key == pygame.K_LEFT and x>0:
                x-=5
                vx=-5
                if l==0:
                    char.state=char.left[0]
                    if count==10:
                        l+=1
                        count=0
                    else:
                        count+=1
                elif l>0 and l<5:
                    char.state=char.left[l]
                    if count==10:
                        l+=1
                        count=0
                    else:
                        count+=1
                if count==10:
                    if l==5:
                        l=0
                    else:
                        l+=1
                else:
                    count+=1
            if event.key == pygame.K_RIGHT and (x+250)<width:
                x+=5
                vx=5
                if l==0:
                    char.state=char.right[0]
                    if count==10:
                        l+=1
                        count=0
                    else:
                        count+=1
                elif l>0 and l<5:
                    char.state=char.right[l]
                    if count==10:
                        l+=1
                        count=0
                    else:
                        count+=1
                if count==10:
                    if l==5:
                        l=0
                    else:
                        l+=1
                else:
                    count+=1

        if k==0 and char.weaponrect[0]==x:                #Shield Controls
            if keys[pygame.K_SPACE]:
                k=1
#Controls end

#Shield Movement
        if k==1:
            char.weaponrect=char.weaponrect.move([10,0])
            if char.weaponrect[0]>1800-125:
                k=0
                #print char.weaponrect[1]+45/125
                t[(char.weaponrect[1]+45)/125]=0
        else:
            char.weaponrect[0]=x
            char.weaponrect[1]=y+20
        u=(y+62)/125
        m[u]=True

        for i in range(8):
            if m[i] and t[i]:
                s[i][0]-=speed

#Road and tank Display
        for i in range(0,1000,125):
            screen.blit(road,(0,i))
            if t[i/125]<1:               # t is the life of the tank.
                continue
            screen.blit(tank,(1800-125,i))

        if k==1:
            screen.blit(char.weapon,char.weaponrect)
# Collision of shield with bullet and tanks
        if not (s[u][0]>=x-10 and s[u][0]<=x+10):
            for i in range(8):
                if m[i]:
                    if char.weaponrect[0]>=(s[i][0]-10) and char.weaponrect[0]<=(s[i][0]+10) and (not(s[i][0]==1800-125)) and char.weaponrect[1]>=i*125 and char.weaponrect[1]<=(i+1)*125:
                        m[i]=False
                        s[i][0]=1800-125
                        k=0
            for i in range(8):
                if m[i] and t[i]:
                    screen.blit(bulletimg,(s[i][0],s[i][1]))
                    if s[i][0]<10:
                        m[i]=False
                        s[i][0]=1800-125

#Collision of bullet with man
        else:
            lives-=1
            s[u][0]=1800-125
            m[u]=False
#CAPTAIN AMERICA DISPLAY
        if lives>0:
            screen.blit(char.state,(x,y))
        else:
            break
        Lives=myfontl.render("Lives:"+str(lives),False,(255,255,255))

#Levels display
        screen.blit(Lives,(0,0))
        if levelc>=0:
            screen.blit(levels,(700,450))
            pygame.time.delay(1000)
            levelc-=1

        if level==5 and 1 not in t:
            break
#Reinitialising of the variables for next level
        elif 1 not in t:
            level+=1
            screen.blit(levels,(700,450))
            k=0
            x=0
            y=0
            l=0
            t=[1,1,1,1,1,1,1,1]
            s=[]
            m=[]
            for i in range(8):
                s.append([1800-125,40 + i*125])
                m.append(False)
            p=1
            lives=3
            speed+=2
            count=10
            levelc=1
        pygame.time.delay(5)
        pygame.display.update()
