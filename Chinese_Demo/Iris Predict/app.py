'''title: Iris 鸢尾花分类
order_name: 001 iris
'''

import simplestart as ss
import os

ss.config.title = "Iris 鸢尾花分类"

# 创建侧边栏导航
left_sidebar = ss.sidebar(position="left")
with left_sidebar:
    ss.md("# Iris 鸢尾花分类")
    ss.space("mb-4")
    ss.write("基于 SimpleStart 的机器学习应用示例")

# 主内容
ss.anchor_point("main-content")
ss.md("## 欢迎使用 Iris 鸢尾花分类应用")
ss.write("这是一个基于 SimpleStart 框架的机器学习应用示例，展示了如何使用 SimpleStart 构建完整的机器学习工作流。")
ss.write("请通过左侧导航栏浏览各个功能模块。")

# 显示封面图片
ss.space("mb-8")
ss.image(
    src="./data/illustration.png",
    width="800px",
    alt="Gemini_Generated_Image"
)
ss.space("mb-4")
ss.text("Gemini Generated Image", tag = "b")