'''title: 交互式预测
order_name: 004 prediction
'''

import simplestart as ss
from sklearn.datasets import load_iris
import numpy as np

#1 页面文本内容

md_content = """

### 交互式预测实验

本页面用于验证训练好的 KNN 模型在推理阶段的实际表现。通过调整输入特征参数，您可以观察模型在不同数据组合下的分类决策及置信度变化。

#### 参数设置与预测

请调整下方滑块以输入鸢尾花的几何特征（单位：cm）。系统将根据您输入的数值，实时计算并显示预测结果。

{slot#slot_slider#此处为滑块组件插槽：包含花萼长度、花萼宽度、花瓣长度、花瓣宽度四个滑块}

---

#### 预测结果

{slot#slot_result#此处为预测结果展示插槽：显示预测品种名称及置信度数值}

#### 预测说明
1. **参数调整**：通过滑块调整花萼和花瓣的尺寸，系统会实时更新预测结果。
2. **模型使用**：预测使用的是在模型训练页面训练的 KNN 模型。
3. **置信度计算**：置信度基于 KNN 算法中最近邻的距离计算得出，值越高表示预测越可靠。
4. **结果解释**：预测结果显示了模型认为最可能的鸢尾花品种及其置信度。

"""

row = ss.row(width = "70%")
row.start()

md = ss.md(md_content)

#2 代码逻辑
ss.session.warning_str = ""
ss.session.sepal_length = 5.0  # 设置合理的初始值
ss.session.sepal_width = 3.3   # 设置合理的初始值
ss.session.petal_length = 1.4  # 设置合理的初始值
ss.session.petal_width = 0.2   # 设置合理的初始值

# 定义鸢尾花品种名称
species_names = ['Setosa', 'Versicolour', 'Virginica']

# 通用的特征变化处理函数
def on_feature_change(event):
    feature_name = event.data["name"]
    
    if feature_name == "petal_width":
        ss.session.petal_width = event.value
    if feature_name == "petal_length":
        ss.session.petal_length = event.value
    if feature_name == "sepal_length":
        ss.session.sepal_length = event.value
    if feature_name == "sepal_width":
        ss.session.sepal_width = event.value

    update_prediction()

def update_prediction():
    if hasattr(ss.store, 'model') and ss.store.model is not None:
        ss.session.warning_str = ""
        # 准备输入数据
        input_data = [[
            ss.session.sepal_length,
            ss.session.sepal_width,
            ss.session.petal_length,
            ss.session.petal_width
        ]]
        
        # 预测
        prediction = ss.store.model.predict(input_data)[0]
        species = species_names[prediction]
        
        # 计算置信度（使用KNN的距离作为简单的置信度指标）
        distances, indices = ss.store.model.kneighbors(input_data)
        confidence = 1.0 / (1.0 + np.mean(distances))  # 简单的置信度计算
        
        # 更新会话变量
        ss.session.prediction = species
        ss.session.confidence = confidence
    else:
        ss.session.warning_str = "请先在模型训练页面训练模型"
        ss.session.prediction = ""
        ss.session.confidence = 0

#ui
# 输入参数
with md.slot("slot_slider"):
    container = ss.container(color = "#fafcff", width = 600, direction = "column")
    container.start()

    # 花萼长度
    ss.text("花萼长度:")
    ss.slider(value=5.0,min=4.0,max=8.0,step=0.1,onchange=on_feature_change,eventData= {"name":"sepal_length"}, show_input=True, marks={4: '4cm', 8: '8cm'})

    
    ss.space("mb-4")
    
    # 花萼宽度
    ss.text("花萼宽度:")
    ss.slider(value=3.3,min=2.0,max=4.5,step=0.1, onchange=on_feature_change,eventData= {"name":"sepal_width"}, show_input=True, marks={2: '2cm', 4.5: '4.5cm'})

    
    ss.space("mb-4")
    
    # 花瓣长度
    ss.text("花瓣长度:")
    ss.slider(value=1.4,min=1.0,max=7.0,step=0.1,onchange=on_feature_change,eventData= {"name":"petal_length"}, show_input=True, marks={1: '1cm', 7: '7cm'})

    
    ss.space("mb-4")
    
    # 花瓣宽度
    ss.text("花瓣宽度:")
    ss.slider(value=0.2,min=0.1,max=2.5,step=0.1,onchange=on_feature_change,eventData= {"name":"petal_width"}, show_input=True, marks={0.1: '0.1cm', 2.5: '2.5cm'})
    container.end()

with md.slot("slot_result"):
    ss.text(f"预测品种: @prediction  置信度: @confidence")
    ss.text("@warning_str", tag = "mark")

row.end()

update_prediction()
