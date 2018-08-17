import pygame
from test5 import *
pygame.init()

screen = pygame.display.set_mode((480,700))
bg = pygame.image.load('./images/background.png')
#bg = pygame.image.load('./images/game_loading1.png')

#screen.blit(bg,(0,0))
#pygame.display.update()
hero = pygame.image.load('./images/hero_blowup_n1.png')
screen.blit(hero,(200,500))

herorect = pygame.Rect(200,500,120,120)
#screen.blit(hero,herorect)


#pygame.display.update()
clock = pygame.time.Clock()#创建时钟

enemy = EnemySprite()
enemy1 = EnemySprite()
enemy2 = EnemySprite()
enemy3 = EnemySprite()
enemy4 = EnemySprite()
enemy5 = EnemySprite()
enemy1.rect.x = 50
#enemy1.rect.y = 100
enemy2.rect.x = 80
enemy2.rect.y = 120
enemy3.rect.x = 130
enemy3.rect.y = 180
enemy4.rect.x = 150
enemy4.rect.y = 200
enemy5.rect.x = 200
enemy5.rect.y = 240
enemy1.speed = 2
enemy2.speed = 5
enemy3.speed = 3
enemy4.speed = 2
enemy5.speed = 4
enemy_group = pygame.sprite.Group(enemy,enemy1,enemy2,enemy3)
while True:
	clock.tick(60)
	herorect.y-=3
	screen.blit(bg,(0,0))
	screen.blit(hero,herorect)

	if herorect.bottom <= 0:
		herorect.top = 700
	enemy_group.update()#更新
	enemy_group.draw(screen)


	for event in pygame.event.get():
		# 判断用户是否点击了关闭按钮
		if event.type == pygame.QUIT:
			print("退出游戏...")
			pygame.quit()
			# 直接退出系统
			exit()
	pygame.display.update()#更新




pygame.quit()

