import pygame
import random
##########################################################################################################
#기본 초기화
pygame.init()

#스크린 설정
screen_width = 480
screen_height = 640
screen = pygame.display.set_mode((screen_width,screen_height))

#스크린 제목 설정
pygame.display.set_caption("Avoiding Poof Game")

clock = pygame.time.Clock()
##########################################################################################################

#배경 이미지 로드
background = pygame.image.load("C:\\MinGW\\bin\\Python\\AvoidingPoofGame\\background.jpg")

#캐릭터 로드
character = pygame.image.load("C:\\MinGW\\bin\\Python\\AvoidingPoofGame\\character.png")
character_size = character.get_rect().size
character_width = character_size[0]
character_height = character_size[1]
character_x_pos = screen_width/2 - character_width/2
character_y_pos = screen_height - character_height

#똥 로드
poop_image = pygame.image.load("C:\\MinGW\\bin\\Python\\AvoidingPoofGame\\poop.png")
poop_size = poop_image.get_rect().size
poop_width = poop_size[0]
poop_height = poop_size[1]

#폰트 설정
game_font = pygame.font.Font(None,40)

#정지 버튼 로드
pause_image = pygame.image.load("C:\\MinGW\\bin\\Python\\AvoidingPoofGame\\pause.png")
pause_size = pause_image.get_rect().size
pause_width = pause_size[0]
pause_height = pause_size[1]
pause_x_pos = screen_width - pause_width - 10
pause_y_pos = 10

#continue button
continue_button = game_font.render("CONTINUE", True, (0,0,0))

def collide_with_point(int x, int y):
    if (x and y)
#Quit button
quit_button = game_font.render("QUIT", True, (0,0,0))

def paused():
    screen.blit(background,(0,0))

    screen.blit(continue_button,(screen_width/3,screen_height/2 - 50))
    
    screen.blit(quit_button,(screen_width/3+43,screen_height/2 + 10))
    
    pygame.display.update()
    
    for event in pygame.event.get():
        if (event.type == pygame.MOUSEBUTTONDOWN and event.button == 1):
            pos = 
    
    
    
    
    
""" poop_x_pos = screen_width/2 - poop_width/2
poop_y_pos = 0 """

#레벨 디자인 - 똥의 개수, 낙하 속도
curr_level = 1
max_level = 6 #0~5
time_per_level = [10*(i+1) for i in range(max_level)]

new_poops_per_level = 3
num_of_poops_for_level = [5+(3*i) for i in range(6)]
poop = [[-1 for j in range(3)] for i in range(num_of_poops_for_level[curr_level-1])]
for i in range(num_of_poops_for_level[curr_level-1]): #똥이 나오는 시간
    poop[i][2] = random.randrange(0,time_per_level[curr_level-1])

#속도 설정
character_to_left = 0
character_to_right = 0
poop_down_speed = 2
speed = 0.3
frame = 30

#시간 설정
start_ticks = pygame.time.get_ticks()

running = True
while running:
    dt = clock.tick(frame)
    for event in pygame.event.get():
        #창을 닫았을 때
        if event.type == pygame.QUIT:
            running = False
        
        #키가 눌려있는 상태일 때
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                character_to_left -= speed
            elif event.key == pygame.K_RIGHT:
                character_to_right += speed
        
        #키를 뗐을 때
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                character_to_left = 0
            elif event.key == pygame.K_RIGHT:
                character_to_right = 0

        #마우스 클릭을 했을 때
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            clicked_pos = pygame.mouse.get_pos()
            if clicked_pos[0] >= pause_x_pos and clicked_pos[0] <= screen_width-10:
                if clicked_pos[1] >= 10 and clicked_pos[1] <= pause_height + 10:
                    time_before_pause = pygame.time.get_ticks()
                    paused()
                    time_after_pause = pygame.time.get_ticks()
                    start_ticks += (time_after_pause - time_before_pause)
                    
            
            
    #캐릭터 이동
    character_x_pos += (character_to_left + character_to_right) * dt
    
    elapsed_time = (pygame.time.get_ticks() - start_ticks) / 1000
    
    #똥 이동
    for i in range(num_of_poops_for_level[curr_level-1]):
        if poop[i][0] == -1 and poop[i][1] == -1 and poop[i][2] < elapsed_time:
            poop[i][0] = random.randrange(0,screen_width-poop_width)
            poop[i][1] = 0 
        elif poop[i][0] == -1 and poop[i][1] == -1:
            continue
            
        #똥 낙하
        poop[i][1] += poop_down_speed
        
        #똥 낙하 완료시 삭제
        if poop[i][1] >= screen_height-poop_height:
            poop[i][0] = -1
            poop[i][1] = -1
            poop[i][2] = random.randrange(int(elapsed_time)+1,int(elapsed_time)+10)

    #가로 경계 처리
    if character_x_pos < 0:
        character_x_pos = 0
    elif character_x_pos > screen_width - character_width:
        character_x_pos = screen_width - character_width
    
    #충돌 처리
    character_rect = character.get_rect()
    character_rect.left = character_x_pos
    character_rect.top = character_y_pos
    
    for i in range(num_of_poops_for_level[curr_level-1]):
        if poop[i][0] == -1 and poop[i][1] == -1:
            continue
        poop_rect = poop_image.get_rect()
        poop_rect.left = poop[i][0]
        poop_rect.top = poop[i][1]
        if character_rect.colliderect(poop_rect):
            running = False
            print("collided")
    
    #시간 계산
    #경과 시간 계산
    elapsed_time = (pygame.time.get_ticks() - start_ticks) / 1000
    
    timer = game_font.render(str(int(elapsed_time)), True, (0,0,0))

    #레벨 갱신
    if elapsed_time > time_per_level[curr_level-1] and curr_level < max_level:
        curr_level += 1
        poop_down_speed += 1
        for i in range(new_poops_per_level):
            temp_x = -1
            temp_y = -1
            temp_time = random.randrange(int(elapsed_time)+1,int(elapsed_time)+10)
            poop.append([temp_x,temp_y,temp_time])
        
    #객체 그리기
    screen.blit(background,(0,0))

    screen.blit(character,(character_x_pos,character_y_pos))

    for i in range(num_of_poops_for_level[curr_level-1]):
        if poop[i][0] != -1 and poop[i][1] != -1:
            screen.blit(poop_image,(poop[i][0],poop[i][1]))
    
    screen.blit(timer,(10,10))

    screen.blit(pause_image,(pause_x_pos,pause_y_pos))
    
    pygame.display.update()

pygame.quit()