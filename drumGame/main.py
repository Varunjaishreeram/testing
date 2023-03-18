import pygame
#from pygame import mixer
pygame.init()

WIDTH=800
HEIGHT=600

black=(0,0,0)
white=(255,255,255)
gray=(128,128,128)
red=(255,0,0)
blue=(0,255,255)
green=(0,255,0)

screen=pygame.display.set_mode((WIDTH,HEIGHT))
Font=pygame.font.SysFont('Roboto-Bold.ttf',40)
pygame.display.set_caption("varun's Drum")

beats=8
clicked=[[-1 for i in range(beats)] for i in range(6)]
active_beats=1
bpm=60
playing=True
active_length=0
beat_changed=True

def drawGrid(clicked,beat):
    boxes=[]
    left_box=pygame.draw.rect(screen,gray,[0,0,120,480],3)
    bottom_box=pygame.draw.rect(screen,gray,[0,480,WIDTH,120],3)
    
    hi_hat_text=Font.render("Hi Hat",True,white)
    screen.blit(hi_hat_text,(20,25))
    snare_text=Font.render("Snare",True,white)
    screen.blit(snare_text,(20,105))
    snare_text=Font.render("Bass Drum",True,white)
    screen.blit(snare_text,(10 ,185))
    snare_text=Font.render("Crash",True,white)
    screen.blit(snare_text,(20,265))
    snare_text=Font.render("Clap",True,white)
    screen.blit(snare_text,(20,345))
    snare_text=Font.render("Snare",True,white)
    screen.blit(snare_text,(20,425))
    
    for i in range(5):
        pygame.draw.line(screen,gray,[0,80*(i+1)],[119,80*(i+1)],4)



    for i in range(8):
        for j in range(6):
            pygame.draw.rect(screen,black,[120+(i*85)-1,j*80+1,85,80],3)
        
            if clicked[j][i]==-1:
                color=gray
            else:
                color=green
        
            rect=pygame.draw.rect(screen,color,[120+(i*85),j*80,85,80],0,3)
            boxes.append((rect,(i,j)))
            
            pygame.draw.rect(screen,red,[120+(i*85)-1,j*80+1,85,80],3)
        
        acrive=pygame.draw.rect(screen,blue,[120+(beat*85),0,85,480],3);


    return boxes
run=True

while run:
    boxes=drawGrid(clicked,active_beats)
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            run=False

        if event.type==pygame.MOUSEBUTTONDOWN:
            for i in range(len(boxes)):
                if boxes[i][0].collidepoint(event.pos):

                    coords=boxes[i][1]
                    clicked[coords[1]][coords[0]]*=-1
    beat_length=3600//bpm
    if playing:
        if active_length<beat_length:
            active_length+=1
        else:
            active_length=0
            if active_beats<beats-1:
                active_beats+=1
                beat_changed=True
            else:
                active_beats=0
                beat_changed=True


    pygame.display.flip()

pygame.quit()