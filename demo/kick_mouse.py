import tkinter as tk
import random

# 定义游戏类
class Game:
    def __init__(self, root, size=5, delay=1000, total_time=10):
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
        # self.root.after(total_time * 1000, self.end_game)  # 一分钟后结束游戏
        self.game_over=False #游戏是否结束
        self.image = tk.PhotoImage(file='test.png')  # 加载图片

    # 更新得分标签
    def update_score_label(self):
        self.score_label['text'] = f'得分: {self.score}'

    # 更新时间标签
    def update_time_label(self):
        self.time_label['text'] = f'剩余时间: {self.time_left} 秒'

    # 更新画布
    def update(self):
        row, col = random.randint(0, self.size-1), random.randint(0, self.size-1)
        if not self.grid[row][col]:  # 如果当前位置没有圆圈
            x1 = col * 80
            y1 = row * 80
            image_item = self.canvas.create_image(x1, y1, anchor='nw', image=self.image)  # 在指定位置创建一个图片
            self.grid[row][col] = image_item  # 将新的图片元素存入列表
            self.root.after(self.delay, self.remove, row, col)  # 延迟一定时间后移除这个图片
        self.canvas.bind("<Button-1>", self.click)  # 绑定鼠标左键点击事件
        if not self.game_over:
            self.root.after(self.delay, self.update)  # 延迟一定时间后更新画布


    # 更新剩余时间
    def update_time(self):
        if self.time_left > 0:  # 如果剩余时间大于0
            self.time_left -= 1  # 剩余时间减一秒
            self.update_time_label()  # 更新时间标签
            self.root.after(1000, self.update_time)  # 延迟一秒后更新剩余时间
        else:
            self.end_game()  # 如果剩余时间为0，则结束游戏

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
        self.game_over=True
        print('游戏结束！')
        self.root.quit()

# 创建主窗口
root = tk.Tk()
# 创建游戏实例
game = Game(root)
# 开始游戏主循环
root.mainloop()
