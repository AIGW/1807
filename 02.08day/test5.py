import random
import pygame
SCREEN_RECT = pygame.Rect(0,0,480,700)
#HERO_FIRE_EVENT = pygame.USEREVENT + 1

CREATE_ENEMY_EVENT = pygame.USEREVENT
class GameSprite(pygame.sprite.Sprite):
	def __init__(self,imagename,speed=1):
		super().__init__()
		self.image = pygame.image.load(imagename)
		self.rect = self.image.get_rect()
		self.speed = speed

	def update(self):
		self.rect.y+=self.speed


class EnemySprite(GameSprite):
	def __init__(self):
		self.imagename = './images/enemy1.png'
		super().__init__(self.imagename)
		self.rect.bottom = 0
		maxvalue = SCREEN_RECT.width - self.rect.width
		self.rect.x = random.randint(0,maxvalue)
		self.speed = random.randint(1,5)
	def update(self):
		super().update()
		#判断敌机是否移除屏幕
		if self.rect.y >= SCREEN_RECT.height:
			#将精灵从所有组中删除
			self.kill()
			print('敌机摧毁')
class BackgroundSprite(GameSprite):
	def __init__(self,is_alt=False):
		self.imagename = './images/background.png'
		super().__init__(self.imagename)
		if is_alt:
			self.rect.y = -self.rect.height
	def update(self):
		super().update()
		if self.rect.top >= SCREEN_RECT.height:
			self.rect.y = -self.rect.height
class Hero(GameSprite):
	"""英雄精灵"""
	def __init__(self):
		self.imagename = './images/hero2.png'
		super().__init__(self.imagename,0)
		self.rect.centerx = SCREEN_RECT.centerx
		self.rect.bottom = SCREEN_RECT.bottom - 120
		self.rect.x += self.speed
		self.bulletgroup = pygame.sprite.Group()
		self.move = False
		print('英雄登场...')
	def update(self):
		# super().update()
		self.rect.x+=self.speed	
		self.rect.y+=self.speed1
		
		if self.rect.left < 0:
			self.rect.left = 0

		elif self.rect.right > SCREEN_RECT.right:
			self.rect.right = SCREEN_RECT.right
		elif self.rect.bottom > SCREEN_RECT.bottom:
			self.rect.bottom = SCREEN_RECT.bottom
		elif self.rect.top < 0:
			self.rect.top = 0	

	def fire(self):
		print('发射子弹...')
		
		bullet = BulletSprite()
		bullet.rect.bottom = self.rect.y - 15
		bullet.rect.centerx = self.rect.centerx
		self.bulletgroup.add(bullet)
		
		bullet = BulletSprite()
		bullet.rect.bottom = self.rect.y +20
		bullet.rect.centerx = self.rect.centerx + 50
		self.bulletgroup.add(bullet)

		bullet = BulletSprite()
		bullet.rect.bottom = self.rect.y +20
		bullet.rect.centerx = self.rect.centerx - 50
		self.bulletgroup.add(bullet)
class BulletSprite(GameSprite):#子弹精灵
	def __init__(self):
		self.imagename = "./images/bullet1.png"	
		super().__init__(self.imagename,-20)
	
	def __del__(self):
		print("子弹销毁了")	

	def update(self):
		super().update()
		if self.rect.bottom <= 0:
			self.kill()		

class Bomb(object):
    # 初始化爆炸
    def __init__(self, scene):
        self.main_scene = scene
        # 加载爆炸资源
        self.image = [pygame.image.load("images/enemy0_down3.png" + str(v) + ".png") for v in range(1, 8)]
        # 设置当前爆炸播放索引
        self.index = 0
        # 图片爆炸播放间隔
        self.interval = 20
        self.interval_index = 0
        # 爆炸位置
        self.position = [0, 0]
        # 是否可见
        self.visible = False
 
    # 设置爆炸播放的位置
    def set_pos(self, x, y):
        self.position[0] = x
        self.position[1] = y
 
    # 爆炸播放
    def action(self):
        # 如果爆炸对象状态不可见，则不计算坐标
        if not self.visible:
            return
 
        # 控制每一帧图片的播放间隔
        self.interval_index += 1
        if self.interval_index < self.interval:
            return
        self.interval_index = 0
 
        self.index = self.index + 1
        if self.index >= len(self.image):
            self.index = 0
            self.visible = False
 
    # 绘制爆炸
    def draw(self):
        # 如果对象不可见，则不绘制
        if not self.visible:
            return
        self.main_scene.scene.blit(self.image[self.index], (self.position[0], self.position[1]))

