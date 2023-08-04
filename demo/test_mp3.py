import pygame

# 初始化pygame模块
pygame.init()

# 加载音乐文件
pygame.mixer.music.load("ddd.mp3")

# 播放音乐
pygame.mixer.music.play()

# 在播放结束前，阻止程序终止
while pygame.mixer.music.get_busy():
    # 设置每次检查的间隔（以毫秒为单位），避免无效的占用过多CPU时间
    pygame.time.Clock().tick(10)
