'''
title: 模型训练
order_name: 003 train
'''
#参考 https://www.kaggle.com/code/nathsubhajit/iris-flower-classification

import simplestart as ss
import time
import pandas as pd
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score, confusion_matrix


# 1. 页面内容 Markdown 格式
# 注意：我们在需要动态显示结果的地方预留了 {slot#xxx#提示文字}
md_content = """
### 模型训练实验室

在开始预测之前，我们需要先“教”计算机如何识别花朵。本页面将展示如何使用 **K近邻算法 (KNN)** 对鸢尾花数据集进行完整的模型训练流程。

#### 1. 核心原理：近朱者赤，近墨者黑
KNN 算法的核心思想非常直观：如果一个样本在特征空间中与 **K 个最相邻** 的样本大多数属于同一类别，那么该样本也属于这个类别。

我们可以这样想象花朵在坐标系中的分布：
- **Setosa**：特征独特，通常独自聚集在一个角落。
- **Versicolor & Virginica**：特征较为相似，两者分布区域会有部分重叠。
- **判别逻辑**：当我们遇到一朵“未知花朵”时，只需观察它**周围最近的 K 个邻居**，得票最多的类别就是它的身份。

#### 2. 实验配置与数据划分
为了科学地评估模型性能，我们遵循机器学习的标准流程——**留出法 (Hold-out)**。我们将 150 条原始数据按照 **7:3** 的比例进行随机切分：

{slot#config#这里将显示参数配置表格}


::: primary
**💡 关于随机种子 (Random State)**
这里的 `Random State` 用于控制数据打乱的随机性。固定该数值（如 42）可以确保每次运行时，训练集和测试集的划分完全一致，从而保证实验结果的**可复现性**。
:::

#### 3. 执行训练
点击下方按钮，程序将自动执行以下步骤：
1.  **数据加载**：读取鸢尾花数据集。
2.  **数据切分**：根据上述配置划分为训练集和测试集。
3.  **模型构建**：初始化 KNN 分类器（设置 K=5）。
4.  **模型拟合**：在训练集上“学习”特征。
5.  **模型评估**：在测试集上进行“考试”并计算准确率。

{slot#train#这里将放置训练按钮}

---

#### 5. 训练结果

{slot#train_result#模型训练的结果将显示在这里...}

---

#### 6. 术语解释与结果解读
- **准确率 (Accuracy)**
    - 定义：模型预测正确的样本数占总样本数的比例。
    - 解读：越接近 1.0 (100%) 代表模型效果越好。

- **混淆矩阵 (Confusion Matrix)**
    - **对角线数值**：代表**预测正确**的数量。数值越大越好（理想状态是全在对角线上）。
    - **非对角线数值**：代表**预测错误**的数量。例如，第二行第三列的数字表示将“Versicolor”错判为“Virginica”的样本数<em style="font-size: small">(随机种子是5的测试结果)</em>，该数值越小越好。
"""

row = ss.row(width="70%")
row.start()

# 渲染 Markdown
md = ss.markdown(md_content)

#2 代码逻辑

# 定义超参数
TEST_SIZE = 0.3
RANDOM_STATE = 42
K_NEIGHBORS = 5

# 构造配置表格的 DataFrame
config_data = {
    '参数名称': ['算法模型', 'K 值 (邻居数)', '训练/测试比例', '随机种子', '距离度量'],
    '设定值': ['KNN (K-Nearest Neighbors)', K_NEIGHBORS, '70% / 30%', "@random_state", 'Minkowski (p=2)'],
    '说明': ['基于距离的分类算法', '决定投票范围的邻居数量', '105个样本用于训练，45个样本用于测试', '固定数据切分方式，确保结果可复现', '即欧几里得距离，计算直线距离']
}

### -----------------------


cm_table = None
ss.session.acc = ""

# 定义训练逻辑
def run_training():
    global cm_table
    #with ss.spinner("模型正在训练中，请稍候..."):
    time.sleep(1.5)  # 模拟耗时操作
    
    # --- 真实的机器学习代码 ---
    iris = load_iris()
    RANDOM_STATE = ss.session.random_state
    X_train, X_test, y_train, y_test = train_test_split(
        iris.data, iris.target, test_size=TEST_SIZE, random_state=RANDOM_STATE)

    
    knn = KNeighborsClassifier(n_neighbors=K_NEIGHBORS)
    #开始训练模型
    knn.fit(X_train, y_train)
    
    # 保存训练好的模型到 Session State，以便在其他地方使用
    ss.store.model = knn
    
    
    y_pred = knn.predict(X_test)
    acc = accuracy_score(y_test, y_pred)
    cm = confusion_matrix(y_test, y_pred)
    print(f"accuracy: {acc:.4f}")
    # -----------------------
    
    # 保存结果到 Session State，以便在其他地方使用
    ss.store.model = knn
    ss.session.acc = f"{acc:.4f}"
    ss.store.cm = cm
    ss.store.model_trained = True
    
    # 更新训练结果显示
    cm_df = pd.DataFrame(cm, index=['Setosa', 'Versicolour', 'Virginica'], 
                        columns=['Setosa', 'Versicolour', 'Virginica'])

    # 更新混淆矩阵表格数据
    cm_table.prop.tableData = cm_df



# config 插槽 -- 显示配置表格
config_df = pd.DataFrame(config_data)
with md.slot("config"):
    ss.table(config_df, width="80%", border=True)


# train 插槽 -- 显示训练按钮
with md.slot("train"):
    ss.button("训练模型", type="primary", onclick=run_training)


# train_result 插槽 -- 显示训练结果显示
with md.slot("train_result"):
    ss.write("**准确率**: @acc")

    ss.write("**混淆矩阵**:")

    # 显示混淆矩阵
    cm_table = ss.table(pd.DataFrame(), width=400, border=True)

row.end()


#侧边栏
import random
ss.session.random_state = 5
def shuffle_random():
    ss.session.random_state = random.randint(1, 1000)

def reset_random_state():
    ss.session.random_state = 5

with ss.sidebar():
    ss.write("当前随机种子: @random_state")
    ss.button("更新随机种子", onclick=shuffle_random)
    ss.button("重置随机种子", onclick=reset_random_state)