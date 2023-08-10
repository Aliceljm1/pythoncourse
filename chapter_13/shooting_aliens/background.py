import pygame

class Background:
    """表示游戏背景的类"""

    def __init__(self, ai_game, speed=1):
        """设置背景的初始位置和速度"""

        # 获取游戏屏幕的信息
        self.screen = ai_game.screen
        self.screen_rect = self.screen.get_rect()

        # 从文件中加载背景图片
        self.image = pygame.image.load('images/bg.png').convert()
        self.rect = self.image.get_rect()

        # 设置背景的初始位置
        self.rect.bottom = self.screen_rect.bottom

        # 创建一个背景图片列表，每个图片的位置不同
        self.backgrounds = []
        for i in range(3):
            # 复制背景图片和位置
            background = {'image': self.image.copy(), 'rect': self.rect.copy()}
            # 设置每个背景图片的位置
            background['rect'].bottom = self.rect.bottom - i * self.rect.height
            self.backgrounds.append(background)

        # 设置背景图片移动的速度
        self.speed = speed

    def update(self):
        """移动背景图片的位置"""
        

        # 遍历每个背景图片
        for background in self.backgrounds:
            # 向下移动背景图片
            background['rect'].move_ip(0, self.speed)
            #TODO 尝试修改move_ip 的两个参数，修改为正数，负数，0，观察背景图片的移动情况
            #TODO 修改代码向下移动的同时，也向左边移动，每次移动1像素
            #TODO 修改代码向下移动的同时，左边移动10像素，右边移动十个像素
            # 如果背景图片完全移出屏幕，则将其移动到最上方
            if background['rect'].top >= self.screen_rect.bottom:
                background['rect'].bottom = self.backgrounds[0]['rect'].top
                # 将移出屏幕的图片放到列表的末尾
                self.backgrounds.append(self.backgrounds.pop(0))

    def blitme(self):
        """在屏幕上绘制背景图片"""
        
        # 遍历每个背景图片并绘制到屏幕上
        for background in self.backgrounds:
            self.screen.blit(background['image'], background['rect'])
