'''title: 项目简介
order_name: 001 introduction
'''

import simplestart as ss

# 数据探索页面的内容排版

md_content = """
### Iris 鸢尾花分类项目

欢迎来到 Iris 数据集探索与分类应用。这是一个基于机器学习的经典入门项目，旨在通过交互式界面帮助用户理解数据特征并预测鸢尾花品种。

---

#### 数据集简介
Iris 数据集由英国统计学家 Ronald Fisher 在 1936 年整理发布，被誉为机器学习领域的 **"Hello World"**。它包含了 150 个样本，分为 3 个不同的鸢尾花品种，每个品种 50 个样本：

1.  **Setosa (山鸢尾)**：花萼较短但较宽，线性可分性最强。
2.  **Versicolor (变色鸢尾)**：特征介于另外两者之间。
3.  **Virginica (维吉尼亚鸢尾)**：通常拥有较大的花瓣和花萼。

{slot#iris_gallery#这里将展示三种鸢尾花的对比图片}

#### 特征说明
每个样本包含 4 个关键的形态特征，我们将利用这些特征进行建模：

| 特征名称 | 英文标识 | 描述 |
| :--- | :--- | :--- |
| **花萼长度** | `sepal length` | 萼片的外部长度 (cm) |
| **花萼宽度** | `sepal width` | 萼片的外部宽度 (cm) |
| **花瓣长度** | `petal length` | 花瓣的长度 (cm) |
| **花瓣宽度** | `petal width` | 花瓣的宽度 (cm) |

---

#### 应用目标
本应用旨在通过三个步骤带你完成数据分析流程：
1.  **数据探索**：可视化分析不同品种在花萼和花瓣尺寸上的分布差异。
2.  **模型训练**：使用 **K-近邻算法 (KNN)** 构建分类模型。
3.  **交互预测**：构建实时界面，输入尺寸即可预测品种。

"""

row = ss.row(width = "70%")  
row.start()

md = ss.markdown(md_content)

# 代码逻辑
with md.slot("iris_gallery"):
    ss.image(
        src="./data/iris.png",
        width="100%",
        alt="Iris 数据集"
    )

    with ss.row(justify="center"):
        ss.text("Iris 图例，来源: ", tag = "b", color = "gray")
        ss.link("Kaggle Learn", href = "https://storage.googleapis.com/kaggle-media/learn/images/RcxYYBA.png", type = "warning")

row.end()