import pygame 

# 뼈대 만들기
pygame.init() 

# 화면 크기 설정
screen_width = 480 
screen_height = 640 
screen = pygame.display.set_mode((screen_width, screen_height))

# 화면 타이틀 설정
pygame.display.set_caption("적을 피해 움직여라!") 

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
to_x = 0 # 가로 방향
to_y = 0 # 세로 방향
 
# 이벤트 루프
running = True 
while running: 
    for event in pygame.event.get():  
        if event.type == pygame.QUIT: 
            running = False 

# 캐릭터 움직이기
        if event.type == pygame.KEYDOWN: # 키가 눌러졌는지 확인
            if event.key == pygame.K_LEFT: # 캐릭터를 왼쪽으로
                to_x -= 1 # 1 위치만큼 왼쪽으로
            elif event.key == pygame.K_RIGHT:
                to_x += 1
            elif event.key == pygame.K_UP: 
                to_y -= 1 # 위로 가면 -
            elif event.key == pygame.K_DOWN:
                to_y += 1

# 캐릭터 멈춰있기               
        if event.type == pygame.KEYUP: # pygame.KEYUP --> 방향키 떼면 멈춤
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT: # 왼쪽이나 오른쪽 키보드에서 떼면
                to_x = 0 # 가로 방향 움직임 멈추기
            elif event.key == pygame.K_UP or event.key == pygame.K_DOWN: # 위나 아래쪽 키보드에서 손을 떼면
                to_y = 0 # 세로 방향 움직임 멈추기


# 캐릭터 좌표 움직일때마다 바꾸기
    character_x_pos += to_x  # (0,0)좌표에서 가로 +1, -1만큼 움직일것
    character_y_pos += to_y  # (0,0)좌표에서 세로 +1, -1만큼 움직일것         

# 화면 밖으로 벗어나지 않게 좌표 조정
# 가로 경계값 처리
    if character_x_pos < 0: # 화면 왼쪽 이전으로 더 나갔다는 소리
        character_x_pos = 0 # 맨왼쪽에 멈추기
    elif character_x_pos > screen_width - character_width: # 오른쪽 끝에 머물게 하기 --> 스크린가로 크기에서 캐릭터 가로 크기 빼야 캐릭터가 화면밖으로 안나감
        character_x_pos = screen_width - character_width

# 세로 경계값 처리
    if character_y_pos < 0: # 화면 위쪽 이전으로 더 나갔다는 소리
        character_y_pos = 0 # 맨 위쪽에 멈추기
    elif character_y_pos > screen_height - character_height: # 오른쪽 끝에 머물게 하기 --> 스크린가로 크기에서 캐릭터 가로 크기 빼야 캐릭터가 화면밖으로 안나감
        character_y_pos = screen_height - character_height

# blit : 좌표 설정 (맨왼쪽, 맨위쪽 기준임)
    screen.blit(background, (0,0))

    screen.blit(character, (character_x_pos, character_y_pos)) 

    pygame.display.update()

# pygame 종료
pygame.quit()