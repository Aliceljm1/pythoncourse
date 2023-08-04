import tkinter as tk
from PIL import Image, ImageTk

root = tk.Tk()

# 创建一个 canvas
canvas = tk.Canvas(root, width=800, height=600, bg='white')
canvas.pack()

# 绘制一个圆形， 尝试修改代码修改圆的大小和位置
canvas.create_oval(50, 50, 150, 150, fill='red')

# 绘制一个矩形
canvas.create_rectangle(200, 50, 300, 150, fill='blue')

# 绘制一条线段
canvas.create_line(350, 50, 450, 150, fill='green')

# 图片间的距离
dis = 50

# 加载第一个图片
image1 = Image.open("imag_baidu.jpg")
photo1 = ImageTk.PhotoImage(image1)

#尝试修改代码，改变图片显示的位置，
canvas.create_image(500, 100, image=photo1)

# 加载第二个图片
image2 = Image.open("image_kaiyuan.jpg")
photo2 = ImageTk.PhotoImage(image2)
canvas.create_image(500 + image1.width + dis, 100, image=photo2)

root.mainloop()
