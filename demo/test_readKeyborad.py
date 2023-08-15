# 导入pygame库
import pygame

# 初始化pygame和其混音器
pygame.init()
pygame.mixer.init()

# 设置窗口的宽度和高度
WIDTH, HEIGHT = 800, 600

# 创建窗口
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("音乐播放器,按下X按键切换歌曲")

# 加载两首歌
songs = ["mp3test/song2.mp3", "mp3test/song1.mp3"]
current_song = 0
# 为歌曲结束设置一个自定义事件
SONG_END = pygame.USEREVENT + 1
pygame.mixer.music.set_endevent(SONG_END)

# 开始播放第一首歌
pygame.mixer.music.load(songs[current_song])
pygame.mixer.music.play()

# 主循环
running = True
while running:
    for event in pygame.event.get():
        # 如果点击了关闭按钮
        if event.type == pygame.QUIT:
            running = False

        # 如果歌曲结束
        elif event.type == SONG_END:
            # 切换到下一首歌
            current_song = (current_song + 1) % len(songs)
            pygame.mixer.music.load(songs[current_song])
            pygame.mixer.music.play()
        # 如果按下了键盘按键
        elif event.type == pygame.KEYDOWN:
            if event.key==13:
                print("enter")
            if event.key == pygame.K_x:  # 如果按键是X
                # 停止当前歌曲
                pygame.mixer.music.stop()

                # 切换到另一首歌
                current_song = current_song + 1
                #TODO 思考：为什么这里要判断current_song是否大于等于len(songs)呢？
                # 请注释如下两行代码，观察运行是否报错
                if(current_song >= len(songs)):
                    current_song = 0
                pygame.mixer.music.load(songs[current_song])
                pygame.mixer.music.play()

# 退出pygame
pygame.quit()
