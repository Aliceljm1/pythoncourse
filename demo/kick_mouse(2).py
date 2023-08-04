import tkinter as tk
import random
import tkinter.messagebox
from PIL import Image, ImageTk


# 定义游戏类
class Game:
    def __init__(self, root, size=5, delay=900, total_time=20):
        self.size = size  # 定义宫格的大小
        self.delay = delay  # 定义每个圆圈显示的时间
        self.score = 0  # 初始化得分
        self.time_left = total_time  # 初始化剩余时间
        self.root = root  # 定义主窗口
        self.colors = ['red', 'green', 'yellow', 'blue']  # 可选颜色列表
        self.score_label = tk.Label(root, text=f'得分: {self.score}')  # 创建得分标签
        self.score_label.pack()
        self.time_label = tk.Label(root, text=f'剩余时间: {self.time_left} 秒')  # 创建时间标签
        self.time_label.pack()
        self.canvas = tk.Canvas(root, width=400, height=400)  # 创建画布
        self.canvas.pack()
        self.grid = [[None]*self.size for _ in range(self.size)]  # 创建一个储存所有圆圈的二维列表
        self.root.after(0, self.update)  # 马上开始更新画布
        self.root.after(1000, self.update_time)  # 每隔一秒更新一次剩余时间
        #self.root.after(total_time * 1000, self.end_game)  # 一分钟后结束游戏
        self.game_over = False

        # 更新得分标签
    def update_score_label(self):
        self.score_label['text'] = f'得分: {self.score}'

    # 更新时间标签
    def update_time_label(self):
        self.time_label['text'] = f'剩余时间: {self.time_left} 秒'

    # 更新画布
    def update(self):
        image2 = Image.open("test.png")
        photo2 = ImageTk.PhotoImage(image2)
        self.canvas.create_image(500, 100, image=photo2)

        row, col = random.randint(0, self.size-1), random.randint(0, self.size-1)
        if not self.grid[row][col]:  # 如果当前位置没有圆圈
            x1 = col * 80
            y1 = row * 80
            x2 = x1 + 80
            y2 = y1 + 80

            oval = self.canvas.create_image(x1,y1,image=photo2) # 在指定位置创建一个圆圈
            self.grid[row][col] = oval  # 将新的圆圈存入列表
            self.root.after(self.delay, self.remove, row, col)  # 延迟一定时间后移除这个圆圈
        self.canvas.bind("<Button-1>", self.click)  # 绑定鼠标左键点击事件
        if not self.game_over:
               self.root.after(self.delay, self.update)  # 延迟一定时间后更新画布

    # 更新剩余时间
    def update_time(self):
        if self.time_left > 0:  # 如果剩余时间大于0
            self.time_left -= 1  # 剩余时间减一秒
            self.update_time_label()  # 更新时间标签
            self.root.after(1000, self.update_time)  # 延迟一秒后更新剩余时间
            if self.score == 15:
              self.time_left += 11
        elif  self.score==30 or self.time_left == 0:
              self.end_game()


    # 移除圆圈
    def remove(self, row, col):
        if self.grid[row][col]:  # 如果当前位置有圆圈
            self.canvas.delete(self.grid[row][col])  # 移除圆圈
            self.grid[row][col] = None  # 将列表中对应位置设为None

    # 处理点击事件
    def click(self, event):
        col = event.x // 80
        row = event.y // 80
        if self.grid[row][col]:  # 如果点击位置有圆圈
            self.score += 1  # 得分加一
            self.update_score_label()  # 更新得分标签
            self.remove(row, col)  # 移除圆圈

    # 结束游戏
    def end_game(self):
        self.game_over= True
        print('游戏结束！')
        if self.score>=30 and self.time_left == 0:
            tkinter.messagebox.showinfo("提示", "you,win!")
        elif self.score<=5 or self.time_left == 0:
            tkinter.messagebox.showinfo("提示","game,over!")
        self.root.quit()

# 创建主窗口
root = tk.Tk()

# 创建游戏实例
game = Game(root)
# 开始游戏主循环
root.mainloop()
