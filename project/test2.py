import pygame,sys
if __name__=="__main__":
    pygame.init()
    pygame.font.init()

myfont=pygame.font.SysFont('Comic Sans MS',200)
myfonto=pygame.font.SysFont('Comic Sans MS',100)
myfontl=pygame.font.SysFont('Comic Sans MS',30)
size = width, height = 1800, 1000
black = 0, 0, 0
speed=[0,0]
screen = pygame.display.set_mode(size)
Menu=myfont.render("MENU",False,(255,0,0))
Start=myfonto.render("START",False,(255,0,0))
Quit=myfonto.render("QUIT",False,(255,0,0))
menubg=pygame.image.load("menu.png")
menubg=pygame.transform.scale(menubg,(1800,1000))
ball = pygame.image.load("captain.png")
road=pygame.image.load("road.png")
road=pygame.transform.scale(road,(1800,125))
roadrect=road.get_rect()
ball= pygame.transform.scale(ball,(125,125))
caprunl=pygame.image.load("caprunl.png")
caprunr=pygame.image.load("caprunr.png")
caprunl=pygame.transform.scale(caprunl,(125,125))
caprunr=pygame.transform.scale(caprunr,(125,125))
cap=ball
ballrect=cap.get_rect()


shield=pygame.image.load("shield.png")
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
time=pygame.time.get_ticks()
bulletimg=pygame.image.load("bullet.png")
bulletimg=pygame.transform.scale(bulletimg,(50,50))
for i in range(8):
    s.append([1800-125,40 + i*125])
    m.append(False)
p=1
men=True
xm=770
ym=430
rectl=270
rectb=120
lives=3

pygame.display.set_caption("Bullet Tanks")
while 1:
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



    while 1:
        for event in pygame.event.get():
            if event.type == pygame.QUIT: sys.exit()
        vx=0
        vy=0
        keys=pygame.key.get_pressed()
        if event.type==pygame.KEYDOWN:
            if event.key == pygame.K_UP and y>0:
                y-=10
                vy=-10
                cap=ball
                l=0
            if event.key == pygame.K_DOWN and (y+125)<height:
                y+=10
                vy=10
                cap=ball
                l=0
            if event.key == pygame.K_LEFT and x>0:
                x-=5
                vx=-5
                if l==0:
                    cap=caprunr
                    l=1
                if cap==caprunl:
                    cap=caprunr
                elif cap==caprunr:
                    cap=caprunl
            if event.key == pygame.K_RIGHT and (x+250)<width:
                x+=5
                vx=5
                if l==0:
                    cap=caprunl
                    l=1
                if cap==caprunl:
                    cap=caprunr
                elif cap==caprunr:
                    cap=caprunl
        if k==0:
            if keys[pygame.K_SPACE]:
                k=1
        if k==1:
            shieldrect=shieldrect.move([4,0])
            if shieldrect[0]>1800-125:
                k=0
                t[shieldrect[1]/125]=0
        else:
            shieldrect[0]=x
            shieldrect[1]=y+20

        ballrect=ballrect.move([vx,vy])
        u=(ballrect[1]+62)/125
        #print pygame.time.get_ticks()-time
       # time=pygame.time.get_ticks()
        if (pygame.time.get_ticks()-time)>=100:
            time=pygame.time.get_ticks()
            m[u]=True

        for i in range(8):
            if m[i]:
                #s[u]=s[u].move([-1,0])
                s[i][0]-=5

        for i in range(0,1000,125):
            screen.blit(road,(0,i))
            if t[i/125]<1:
                continue
            screen.blit(tank,(1800-125,i))

        if k==1:
            screen.blit(shield,shieldrect)

        if not (s[u][0]>=x-10 and s[u][0]<=x+10):
            for i in range(8):
                if m[i]:
                    if shieldrect[0]>=(s[i][0]-10) and shieldrect[0]<=(s[i][0]+10) and (not(s[i][0]==1800-125)) and shieldrect[1]>=i*125 and shieldrect[1]<=(i+1)*125:
                        m[i]=False
                        s[i][0]=1800-125
                        k=0
            for i in range(8):
                if m[i]:
                    screen.blit(bulletimg,(s[i][0],s[i][1]))
                    if s[i][0]<10:
                        m[i]=False
                        s[i][0]=1800-125
        else:
            lives-=1
            s[u][0]=1800-125
            m[u]=False

        if lives>0:
            screen.blit(cap,(x,y))
        else:
            break
        Lives=myfontl.render("Lives:"+str(lives),False,(255,255,255))
        screen.blit(Lives,(0,0))
        pygame.display.update()
        pygame.time.delay(5)
