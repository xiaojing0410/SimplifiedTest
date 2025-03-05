
from tkinter import *
import tkinter as tk
import tkinter.font as tkFont



# 配置操作页面
class Warehousing:
    def __init__(self, parent_frame):
        self.frame = parent_frame
        self.content_frame = tk.Frame(self.frame)
        self.content_frame.pack(fill=tk.BOTH, expand=True)

        # ip
        self.ip_group_frame = tk.Frame(self.content_frame)
        self.ip_group_frame.pack(fill='x',pady=(70,0))
        ip_label = Label(self.ip_group_frame, text="ip:", font=('Arial', 14))
        ip_label.pack(side='left', padx=(90,10))
        ip_entry = Entry(self.ip_group_frame)
        ip_entry.pack(side='left', padx=5, fill='x', expand=True)

        # scene_path
        self.scene_path_group_frame = tk.Frame(self.content_frame)
        self.scene_path_group_frame.pack(fill='x')
        scene_label = Label(self.scene_path_group_frame, text='scene_path:', font=('Arial', 14))
        scene_label.pack(side='left', padx=10)
        scene_entry = Entry(self.scene_path_group_frame)
        scene_entry.pack(side='left', padx=5, fill='x', expand=True)




# 测试页面
class Warehousing_enquire:
    def __init__(self, parent_frame):
        self.frame = parent_frame
        self.content_frame = tk.Frame(self.frame)
        self.content_frame.pack(fill=tk.BOTH, expand=True)

        # 测试场景
        self.scene_group_frame = tk.Frame(self.content_frame)
        self.scene_group_frame.pack(fill='x', pady=(70, 0))
        scene_label = Label(self.scene_group_frame, text="测试场景:", font=('Arial', 14))
        scene_label.pack(side='left', padx=(10, 10))
        scene_entry = Entry(self.scene_group_frame)
        scene_entry.pack(side='left', padx=5)
        scene_check = Checkbutton(self.scene_group_frame)
        scene_check.pack(side='left', padx=5)

        # 随机发单
        self.random_set_order_group_frame = tk.Frame(self.content_frame)
        self.random_set_order_group_frame.pack(fill='x', pady=(10, 0))
        random_set_order_label = Label(self.random_set_order_group_frame, text="随机发单:", font=('Arial', 14))
        random_set_order_label.pack(side='left', padx=10)
        random_set_order_check = Checkbutton(self.random_set_order_group_frame)
        random_set_order_check.pack(side='left', padx=5)
        order_count_label = Label(self.random_set_order_group_frame, text="持续发单量:", font=('Arial', 14))
        order_count_label.pack(side='left', padx=(10, 10))
        order_count_entry = Entry(self.random_set_order_group_frame)
        order_count_entry.pack(side='left', padx=5)

        # 添加测试项
        self.case_item_frame = tk.Frame(self.content_frame)
        self.case_item_frame.pack(fill='x', pady=(10,0))
        add_case_item = Button(self.case_item_frame, text='添加测试项', font=('楷体', 14))
        add_case_item.pack()

        # 具体的每个测试项
        self.canvas = tk.Canvas(self.case_item_frame, height=700, width=700, highlightthickness=2, highlightbackground="black")
        self.canvas.pack(pady=(10,0))

        self.buttons_group = Frame(self.canvas)
        # self.buttons_group.pack(fill='x')
        self.canvas.create_window(200,30,window=self.buttons_group)

        # 添加测试
        add_case_button = tk.Button(self.buttons_group, text="添加测试",font=('楷体', 14), command=lambda: print("添加测试"))
        add_case_button.pack(side="left", padx=(5,0))

        # 添加自定义测试
        add_customize_case_button = tk.Button(self.buttons_group, text="添加自定义测试",font=('楷体', 14), command=lambda: print("添加自定义测试"))
        add_customize_case_button.pack(side="left", padx=(5,0))

        # 执行
        run_button = tk.Button(self.buttons_group, text="执行",font=('楷体', 14), command=lambda: print("执行"))
        run_button.pack(side="left", padx=(5,0))

        # 删除
        delete_button = tk.Button(self.buttons_group, text="删除",font=('楷体', 14), command=lambda: print("删除"))
        delete_button.pack(side="left", padx=(5,0))

        self.case_group = Frame(self.canvas)
        self.canvas.create_window(200, 60, window=self.case_group)

        # 语句：LM1511:Wait
        case_text = Entry(self.case_group)
        case_text.pack(padx='0',pady='0',side='left')

        # 执行
        run_button = tk.Button(self.buttons_group, text="执行", font=('楷体', 14), command=lambda: print("执行"))
        run_button.pack(side="left", padx=(5, 0))

        # 删除
        delete_button = tk.Button(self.buttons_group, text="删除", font=('楷体', 14), command=lambda: print("删除"))
        delete_button.pack(side="left", padx=(5, 0))


# 机器人操作页面
class Chuku:
    def __init__(self, parent_frame):
        self.frame = parent_frame
        self.clear_frame()  # 清除现有内容
        self.content_frame = tk.Frame(self.frame)
        self.content_frame.pack(fill=tk.BOTH, expand=True)

        label = tk.Label(self.content_frame, text="出库操作", font=('楷体', 20))
        label.pack(pady=50)

        # 在这里添加出库操作的内容

        # 返回按钮
        back_button = tk.Button(self.content_frame, text="返回", font=('楷体', 15), command=lambda: self.show_start_page(self.frame))
        back_button.pack()

    def clear_frame(self):
        for widget in self.frame.winfo_children():
            widget.destroy()

    def show_start_page(self, parent_frame):
        StartPage(parent_frame)


# 主页面
class StartPage:
    def __init__(self, parent_window):
        self.window = parent_window
        self.window.title('SimpleTest')
        self.window.geometry('800x800+150+150')

        # 创建主frame
        self.frame = tk.Frame(self.window)
        self.frame.pack(fill=tk.BOTH, expand=True)

        # 上方四个按钮
        Button(self.window, text="配置", font=tkFont.Font(size=10), command=lambda: self.show_frame(Warehousing), width=5, height=2, fg='white', bg='gray').place(x=10, y=10)
        Button(self.window, text="测试", font=tkFont.Font(size=10), command=lambda: self.show_frame(Warehousing_enquire), width=5, height=2, fg='white', bg='gray').place(x=60, y=10)
        Button(self.window, text="机器人", font=tkFont.Font(size=10), command=lambda: self.show_frame(Chuku), width=5, height=2, fg='white', bg='gray').place(x=110, y=10)
        Button(self.window, text="关闭", font=tkFont.Font(size=10), command=self.window.destroy, width=5, height=2, fg='white', bg='gray').place(x=160, y=10)

        # 横线隔开内容
        canvas = tk.Canvas(self.window, height=2, bg='black')
        canvas.place(x=0,y=50,relwidth=1) #relwidth=1 可以让 canvas横向自适应窗口宽度
        # tk.Canvas(self.window, height=2, bg='black').pack(fill='x')

        # self.show_start_page()
        self.show_frame(Warehousing_enquire)
        # 让程序主窗体一直运行，直到你主动×掉它
        self.window.mainloop()

    def show_frame(self, frame_class):
        for widget in self.frame.winfo_children():
            widget.destroy()  # 清空现有内容
        frame_class(self.frame)  # 创建新的frame并显示

    def show_start_page(self):
        self.clear_frame()  # 清除现有内容
        start_page_frame = tk.Frame(self.frame)
        start_page_frame.pack(fill=tk.BOTH, expand=True)
        label = tk.Label(start_page_frame, text="欢迎使用", font=("楷体", 30))
        label.pack(pady=100)

    def clear_frame(self):
        for widget in self.frame.winfo_children():
            widget.destroy()

if __name__ == "__main__":
    root = tk.Tk()
    app = StartPage(root)
