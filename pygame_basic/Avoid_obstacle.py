import pygame 

# 뼈대 만들기
pygame.init() 

# 화면 크기 설정
screen_width = 480 
screen_height = 640 
screen = pygame.display.set_mode((screen_width, screen_height))

# 화면 타이틀 설정
pygame.display.set_caption("적을 피해 움직여라!") 

# 배경 이미지 불러오기 (그림판에 배경 만들었음)
# 파일에 background.png 눌러 오른쪽 마우스 --> copy path (주소 복사) 해서 load()안에 넣기
background = pygame.image.load("C:\\Users\\82105\\Desktop\\PythonWorksapce\\pygame_basic\\background.png") # 역슬래쉬 하나씩 더 추가

# 이벤트 루프
running = True 
while running: 
    for event in pygame.event.get():  
        if event.type == pygame.QUIT: 
            running = False 
#   screen.fill((0,0,225) --> 밑에 screen.blit(background, (0,0))를 대신해서 색을 채울 수 있는 문법(알아두기만 하기)

# blit : 배경 그리기 백그라운드가 어디에 나타날지 좌표 설정 (맨왼쪽, 맨위쪽 기준임)
    screen.blit(background, (0,0)) # (0,0) --> 위치: 0만큼 왼쪽, 0만큼 위아래

# 매번 매 프레임마다 화면을 새로 그려주는 동작을 해야함 = pygame.display.update()
# while부분을 계속 돌리며 계속 update해야함
    pygame.display.update() # 게임 화면 다시 그리기! (반드시 필요)

# pygame 종료
pygame.quit()