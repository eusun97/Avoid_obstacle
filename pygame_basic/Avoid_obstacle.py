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

# 캐릭터(스트라이트) 불러오기
character = pygame.image.load("C:\\Pygame_basic\\pygame_basic\\character.png")
character_size = character.get_rect().size 
character_width = character_size[0] 
character_height = character_size[1]
character_x_pos = (screen_width / 2) - (character_width / 2) 
character_y_pos = screen_height - character_height 

# 이동할 좌표 (캐릭터 움직이기)
to_x = 0 
to_y = 0 

# 캐릭터 이동 속도 1 고정 함수
character_speed = 1
 
# 이벤트 루프
running = True 
while running: 
    dt = clock.tick(60) # dt : 델타, 게임화면의 초당 프레임 수를 60으로 설정 : 높게설정하면 부드러움

# 캐릭터가 1초 동안에 00만큼 이동을 해야함
# 10 fps : 1초 동안에 10번 동작 --> 1번에 몇 만큼 이동해야함? --> 10. 10 * 10 = 100
# 20 fps : 1초 동안에 20번 동착 --> 5 * 20 

    print("fps : " + str(clock.get_fps())) # 현재 fps 를 출력해줌

    for event in pygame.event.get():  
        if event.type == pygame.QUIT: 
            running = False 

# 캐릭터 움직이기
        if event.type == pygame.KEYDOWN: 
            if event.key == pygame.K_LEFT: 
                to_x -= 1 
            elif event.key == pygame.K_RIGHT:
                to_x += 1
            elif event.key == pygame.K_UP: 
                to_y -= 1 
            elif event.key == pygame.K_DOWN:
                to_y += 1

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

# blit : 좌표 설정 (맨왼쪽, 맨위쪽 기준임)
    screen.blit(background, (0,0))

    screen.blit(character, (character_x_pos, character_y_pos)) 

    pygame.display.update()

# pygame 종료
pygame.quit()