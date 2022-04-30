import pygame 

# 뼈대 만들기
pygame.init() 

# 화면 크기 설정
screen_width = 480 
screen_height = 640 
screen = pygame.display.set_mode((screen_width, screen_height))

# 화면 타이틀 설정
pygame.display.set_caption("적을 피해 움직여라!") 

# FPS
clock = pygame.time.Clock()

# 배경 이미지 불러오기
background = pygame.image.load("C:\\Pygame_basic\\pygame_basic\\background.png")

# 캐릭터(스프라이트) 불러오기
character = pygame.image.load("C:\\Pygame_basic\\pygame_basic\\character.png")
character_size = character.get_rect().size 
character_width = character_size[0] 
character_height = character_size[1]
character_x_pos = (screen_width / 2) - (character_width / 2) 
character_y_pos = screen_height - character_height 

# 이동할 좌표 (캐릭터 움직이기)
to_x = 0 
to_y = 0 

# 캐릭터 이동 속도 10 고정 함수
character_speed = 1

# 적(enemy) 캐릭터 불러오기
enemy = pygame.image.load("C:\\Pygame_basic\\pygame_basic\\enemy.png")
enemy_size = enemy.get_rect().size 
enemy_width = enemy_size[0] 
enemy_height = enemy_size[1]
enemy_x_pos = (screen_width / 2) - (enemy_width / 2) 
enemy_y_pos = (screen_height / 2) - (enemy_height / 2) 
 
# 폰트 정의
game_font = pygame.font.Font(None, 40) # 폰트 객체 생성(폰트, 크기) None : 디폴트값 적용됨

# 총 시간
total_time = 10 # 10초로 가정

# 시작 시간 정보 
start_ticks = pygame.time.get_ticks() # 현재 tick 정보를 받아옴

# 이벤트 루프
running = True 
while running: 

    dt = clock.tick(60)

    for event in pygame.event.get():  
        if event.type == pygame.QUIT: 
            running = False 

# 캐릭터 움직이기
        if event.type == pygame.KEYDOWN: 
            if event.key == pygame.K_LEFT: 
                to_x -= character_speed 
            elif event.key == pygame.K_RIGHT:
                to_x += character_speed
            elif event.key == pygame.K_UP: 
                to_y -= character_speed
            elif event.key == pygame.K_DOWN:
                to_y += character_speed

# 캐릭터 멈춰있기               
        if event.type == pygame.KEYUP: 
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT: 
                to_x = 0 
            elif event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                to_y = 0 


# 캐릭터 좌표 움직일때마다 바꾸기
# 프레임 수를 높게하나 낮게 하나 게임 속도는 변하지 않게 하기 위해 dt를 곱해줌
    character_x_pos += to_x * dt 
    character_y_pos += to_y * dt   

# 화면 밖으로 벗어나지 않게 좌표 조정
# 가로 경계값 처리
    if character_x_pos < 0: 
        character_x_pos = 0 
    elif character_x_pos > screen_width - character_width: 
        character_x_pos = screen_width - character_width

# 세로 경계값 처리
    if character_y_pos < 0: 
        character_y_pos = 0 
    elif character_y_pos > screen_height - character_height: 
        character_y_pos = screen_height - character_height

# 충돌 처리
    # 실제로 화면상 위치하고 있는 캐릭터의 rect정보를 업데이트 되는 것
    # 충돌 처리를 위한 rect 정보 업데이트
    character_rect = character.get_rect() 
    character_rect.left = character_x_pos 
    character_rect.top = character_y_pos 

# 적 캐릭터도 똑같이 충돌 처리
    enemy_rect = enemy.get_rect()
    enemy_rect.left = enemy_x_pos 
    enemy_rect.top = enemy_y_pos

# 충돌 체크
    if character_rect.colliderect(enemy_rect): 
        print("충돌했습니다.")
        running = False 


# blit : 좌표 설정 (맨왼쪽, 맨위쪽 기준임)
    screen.blit(background, (0,0))
    screen.blit(character, (character_x_pos, character_y_pos)) 
    screen.blit(enemy, (enemy_x_pos, enemy_y_pos)) 

# 타이머 집어 넣기
# 경과 시간 계산 elapsed_time : 지금까지 흘러간 시간 정보
#  흘러간 시간 = 현재 틱 정보 - 시작 틱
    elapsed_time = (pygame.time.get_ticks() - start_ticks) / 1000 # 1000으로 나눠서 초 단위로 표시

    # render 뒤에 들어가는 것은 시간(출력할 글자), True, 글자 색상
    timer = game_font.render(str(int(total_time - elapsed_time)), True, (255,255,255)) # 10 9 8 7 6 이런식으로 흘러가게
    
# 스크린에 표시되는 함수와 좌표 정보
    screen.blit(timer, (10,10))

# 만약 시간이 흘러가다 0 이하가 되면 게임 종료(-1 로 넘어가지않게)
    if total_time - elapsed_time <= 0:
        print("타임 아웃")
        running = False

    pygame.display.update()

# 종료 되기 직전에 잠시 대기 (바로 꺼지지 않게)
pygame.time.delay(2000) # 2초정도 대기 (ms)

# pygame 종료
pygame.quit()