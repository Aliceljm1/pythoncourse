import pygame
import random
def music(self):
    music_array = ["ddd.mp3"]
    index = random.randint(0, len(music_array) - 1)
    # file = Tools.get_resource_mp3_path() + os.sep +  music_array[index]
    file = "C:\\Users\\C30\\Desktop\\aaa" + os.sep + music_array[index]
    pygame.mixer.init()
    pygame.mixer.music.load(file)
    pygame.mixer.music.play(loops=10)  # pygame.mixer.music.play(-1)
    while pygame.mixer.music.get_busy():  # 在音频播放为完成之前不退出程序
        pygame.time.Clock().tick(10)
        pass
music()