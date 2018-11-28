import pygame,sys
if __name__=="__main__":
    pygame.init()
    pygame.font.init()
class Character:
    def __init__(self,left,right,stand,weapon):
        self.left=left
        self.right=right
        self.stand=stand
        self.state=stand
        self.weapon=weapon

myfont=pygame.font.SysFont('Comic Sans MS',200)
myfonto=pygame.font.SysFont('Comic Sans MS',100)
myfontl=pygame.font.SysFont('Comic Sans MS',30)
size = width, height = 1800, 1000
black = (0, 0, 0)

screen = pygame.display.set_mode(size)
#Fonts
Menu=myfont.render("MENU",False,(255,0,0))
Start=myfonto.render("START",False,(255,0,0))
Quit=myfonto.render("QUIT",False,(255,0,0))
#Menu background
menubg=pygame.image.load("menu.png")
menubg=pygame.transform.scale(menubg,(1800,1000))
#Captain stationary is caps
caps= pygame.image.load("cap/captain.png")
#Road
road=pygame.image.load("road.png")
road=pygame.transform.scale(road,(1800,125))
roadrect=road.get_rect()
caps= pygame.transform.scale(caps,(125,125))
#Cap is the state of the characters
cap=caps
capr=[pygame.image.load("cap/capr1.png"),pygame.image.load("cap/capr2.png"),pygame.image.load("cap/capr3.png"),pygame.image.load("cap/capr4.png"),pygame.image.load("cap/capr5.png"),pygame.image.load("cap/capr6.png")]
capl=[pygame.image.load("cap/capl1.png"),pygame.image.load("cap/capl2.png"),pygame.image.load("cap/capl3.png"),pygame.image.load("cap/capl4.png"),pygame.image.load("cap/capl5.png"),pygame.image.load("cap/capl6.png")]
for i in range(6):
    capr[i]=pygame.transform.scale(capr[i],(125,125))
    capl[i]=pygame.transform.scale(capl[i],(125,125))
shield=pygame.image.load("cap/shield.png")
shield=pygame.transform.scale(shield,(90,90))
shieldrect=shield.get_rect()
tank=pygame.image.load("tank.png")
tank=pygame.transform.scale(tank,(125,125))
k=0
x=0
y=0
l=0
t=[1,1,1,1,1,1,1,1]
s=[]
m=[]
time=pygame.time.Clock()
bulletimg=pygame.image.load("bullet.png")
bulletimg=pygame.transform.scale(bulletimg,(50,50))
for i in range(8):
    s.append([1800-125,40 + i*125])
    m.append(False)
p=1
xm=770
ym=430
rectl=270
rectb=120
lives=3
count=10
level=1
levelc=1
speed=1

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
    #Character Choosing
    '''
    while 1:
        for event in pygame.event.get():
            if event.type == pygame.QUIT: sys.exit()
        keys=pygame.key.get_pressed()
        r=0
        l=0
        caps=pygame.transform.scale(caps,(400,400))
        if keys[pygame.K_RIGHT]:
            r=1
        if keys[pygame.K_LEFT]:
            l=1
        screen.blit(menubg,(0,0))
        screen.blit(caps,(750,300))
        pygame.display.update()
'''
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
    speed=1
    caps=pygame.transform.scale(caps,(125,125))
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
                cap=caps
                l=0
            if event.key == pygame.K_DOWN and (y+125)<height:
                y+=10
                vy=10
                cap=caps
                l=0
            if event.key == pygame.K_LEFT and x>0:
                x-=5
                vx=-5
                if l==0:
                    cap=capl[0]
                    if count==10:
                        l+=1
                        count=0
                    else:
                        count+=1
                elif l>0 and l<5:
                    cap=capl[l]
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
                    cap=capr[0]
                    if count==10:
                        l+=1
                        count=0
                    else:
                        count+=1
                elif l>0 and l<5:
                    cap=capr[l]
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

        if k==0 and shieldrect[0]==x:                #Shield Controls
            if keys[pygame.K_SPACE]:
                k=1
#Controls end

#Shield Movement
        if k==1:
            shieldrect=shieldrect.move([10,0])
            if shieldrect[0]>1800-125:
                k=0
                t[shieldrect[1]/125]=0
        else:
            shieldrect[0]=x
            shieldrect[1]=y+20
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
            screen.blit(shield,shieldrect)
# Collision of shield with bullet and tanks
        if not (s[u][0]>=x-10 and s[u][0]<=x+10):
            for i in range(8):
                if m[i]:
                    if shieldrect[0]>=(s[i][0]-10) and shieldrect[0]<=(s[i][0]+10) and (not(s[i][0]==1800-125)) and shieldrect[1]>=i*125 and shieldrect[1]<=(i+1)*125:
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
            screen.blit(cap,(x,y))
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
            speed+=1
            count=10
            levelc=1
        pygame.time.delay(5)
        pygame.display.update()
