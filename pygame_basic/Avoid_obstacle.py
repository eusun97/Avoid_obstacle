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
background = pygame.image.load("C:\Pygame_basic\pygame_basic\\background.png")

# 캐릭터(스트라이트) 불러오기 (그림판에 character.png)
character = pygame.image.load("C:\Pygame_basic\pygame_basic\\character.png")
character_size = character.get_rect().size # 이미지 크기를 구해옴
character_width = character_size[0] # 첫번째 위치에 있는 값이 가로 크기가 됨
character_height = character_size[1]
character_x_pos = (screen_width / 2) - (character_width / 2) # 가로 위치 : 화면 가로의 절반 --> 정중앙, 480/2로 왼쪽기준으로 그려지기에 캐릭터 크기 70의 반을 빼야함
character_y_pos = screen_height - character_height # 세로 위치 : 세로 가장 아래에 해당하는 위치(640위치), 전체높이에서 캐릭터 높이만큼 빼기
 
# 이벤트 루프
running = True 
while running: 
    for event in pygame.event.get():  
        if event.type == pygame.QUIT: 
            running = False 

# blit : 좌표 설정 (맨왼쪽, 맨위쪽 기준임)
    screen.blit(background, (0,0))

    screen.blit(character, (character_x_pos, character_y_pos)) # 캐릭터 그리기

    pygame.display.update()

# pygame 종료
pygame.quit()