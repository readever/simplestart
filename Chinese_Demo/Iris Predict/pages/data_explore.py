'''title: 数据探索
order_name: 002 data_exploration
'''

import simplestart as ss
from sklearn.datasets import load_iris
import pandas as pd

# 数据探索页面的内容排版
md_content = """
### 鸢尾花数据集探索分析

#### 1. 数据概览
这是机器学习中经典的分类数据集，包含了 3 种不同品种的鸢尾花各 50 朵，共 150 个样本。
我们首先来看一下原始数据的前几行：

{slot#data_table#这里将显示前20行数据}

---

#### 2. 特征分布可视化：花萼长宽关系
为了直观地理解不同品种在形态上的差异，我们选取了 **花萼长度** 和 **花萼宽度** 这两个特征进行散点图分析。

请观察下方的散点图：

{slot#scatter_plot#这里将显示散点图，展示不同品种的花萼长宽关系。}

::: primary
**💡 解读**
**蓝色点 (Setosa)**：聚集在左上角，说明山鸢尾的花萼通常较短但较宽, 比较容易将其与其他两类区分开。
**橙色点 (Versicolor) & 绿色点 (Virginica)**：主要分布在右下侧，且两者在分布上存在一定的重叠。
:::

---

#### 3. 统计特征分析
除了可视化，我们还计算了数值特征的统计摘要。下表展示了各个特征的均值、标准差、最小值和最大值。

{slot#describe_table#这里将显示数值特征的统计摘要。}

---

#### 4. 结论
通过上述探索，我们可以发现 **Setosa** 品种在线性可分性上表现最好，仅凭花萼的长宽就能很容易将其与其他两类区分开。而对于 **Versicolor** 和 **Virginica**，可能需要引入花瓣（Petal）的相关特征才能获得更好的分类效果。

"""

row = ss.row(width = "70%")  
row.start()

md = ss.markdown(md_content)


# 代码逻辑

# 加载 Iris 数据集
iris = load_iris()
df = pd.DataFrame(data=iris.data, columns=iris.feature_names)
df['species'] = iris.target
df['species'] = df['species'].map({0: 'Setosa', 1: 'Versicolour', 2: 'Virginica'})


# 显示数据表格（前20行）
with md.slot("data_table"):
    # 使用 simplestart 的表格组件，或者直接显示 pandas 样式
    ss.table(tableData=df.head(20), width = 800, height = 250, stripe=True)

# 显示散点图（花萼长宽关系）
with md.slot("scatter_plot"):
    # 使用 simplestart 的散点图组件
 
    # 准备散点图数据
    x_data = df['sepal length (cm)'].tolist()
    y_data = df['sepal width (cm)'].tolist()
    hue_data = df['species'].tolist()

    # 绘制散点图（使用 hue_data 参数）
    ss.plot.scatter(
        x=x_data,
        y=y_data,
        title="Iris 散点图",
        x_label="花萼长度 (cm)",
        y_label="花萼宽度 (cm)",
        hue_data=hue_data,
        width="700px",
        height="500px"
    )
    
# 显示统计特征分析表格
with md.slot("describe_table"):
    # 计算统计摘要并添加中位数列
    describe_df = df.describe()
    # 对数值进行四舍五入，保留2位小数
    describe_df = describe_df.round(2)

    # 将索引转换为列，以便在表格中显示
    describe_df_reset = describe_df.reset_index()
    # 重命名索引列
    describe_df_reset = describe_df_reset.rename(columns={'index': '统计指标'})
    
    # 准备列配置
    columns = [{'prop': '统计指标', 'label': '统计指标'}]
    for col in describe_df_reset.columns[1:]:
        columns.append({'prop': col, 'label': col})
    
    # 转换为表格数据格式
    table_data = describe_df_reset.to_dict('records')
    
    # 使用 simplestart 的表格组件
    ss.table(tableData=table_data, columns=columns, width=800, stripe=True)

row.end()