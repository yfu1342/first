from kivy.app import App
from kivy.uix.label import Label

# 创建一个 App 类
class HelloWorldApp(App):
    def build(self):
        # 返回一个显示 "Hello, World!" 的标签控件
        return Label(
            text="Hello, World!",
            font_size=50,          # 字体大小
            color=(1, 0.5, 0, 1)   # 橙色 (RGBA)
        )

# 运行 App
if __name__ == '__main__':
    HelloWorldApp().run()