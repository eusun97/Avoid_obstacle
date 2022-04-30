import pygame 

# 뼈대 만들기
pygame.init() 

# 화면 크기 설정
screen_width = 480 
screen_height = 640 
screen = pygame.display.set_mode((screen_width, screen_height))

# 화면 타이틀 설정
pygame.display.set_caption("적을 피해 움직여라!") 

# FPS : 초당 프레임 수 (프레임 수가 높으면 부드러움, 낮으면 끊기거나 덜 부드러움)
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
enemy_x_pos = (screen_width / 2) - (enemy_width / 2) # 적 시작 지점을 화면 가로 중앙에
enemy_y_pos = (screen_height / 2) - (enemy_height / 2) # 적 시작 지점 세로 중앙
 
# 이벤트 루프
running = True 
while running: 
    dt = clock.tick(60)
    print("fps : " + str(clock.get_fps())) 

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
    character_rect = character.get_rect() # character_rect 변수에 캐릭터가 가지는 rect 정보를 가져옴 : 좌표, 가로 세로 정보
    character_rect.left = character_x_pos # 이미지 왼쪽
    character_rect.top = character_y_pos # # 이미지 위쪽

# 적 캐릭터도 똑같이 충돌 처리
    enemy_rect = enemy.get_rect()
    enemy_rect.left = enemy_x_pos 
    enemy_rect.top = enemy_y_pos

# 충돌 체크
    if character_rect.colliderect(enemy_rect): # colliderect : 사각형 기준으로 충돌이 있었는지
        print("충돌했습니다.")
        running = False # 게임 종료 됨


# blit : 좌표 설정 (맨왼쪽, 맨위쪽 기준임)
    screen.blit(background, (0,0))
    screen.blit(character, (character_x_pos, character_y_pos)) 
    screen.blit(enemy, (enemy_x_pos, enemy_y_pos)) # 적 캐릭터 그리기

    pygame.display.update()

# pygame 종료
pygame.quit()