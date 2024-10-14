from sklearn.metrics import confusion_matrix, accuracy_score, precision_score, recall_score, f1_score
import matplotlib.pyplot as plt
import numpy as np

plt.rcParams['font.sans-serif'] = ['SimHei']  # 用来正常显示中文标签
plt.rcParams['axes.unicode_minus'] = False  # 用来正常显示负号

# 定义实际标签和预测标签
y_true = [False] * 98 + [True] * 2  # 100个人的实际结果，98个阴性（False），2个阳性（True）
y_pred = [False] * 94 + [True] * 6  # 模型预测结果，94个阴性（False），6个阳性（True）

# 计算混淆矩阵
conf_matrix = confusion_matrix(y_true, y_pred, labels=[True, False])

# 打印混淆矩阵
print("混淆矩阵:")
print(conf_matrix)

# 计算分类指标
accuracy = accuracy_score(y_true, y_pred)
precision = precision_score(y_true, y_pred, pos_label=True)  # 指定正类标签为True
recall = recall_score(y_true, y_pred, pos_label=True)
f1 = f1_score(y_true, y_pred, pos_label=True)

# 打印分类指标
print("准确率（Accuracy）:", accuracy)
print("精确率（Precision）:", precision)
print("召回率（Recall）:", recall)
print("F1分数（F1 Score）:", f1)

true_classes = ['False', 'True']  # 真实标签
predicted_classes = ['Negative', 'Positive']  # 预测标签


# 可视化混淆矩阵
def plot_confusion_matrix(cm, title='Confusion matrix', cmap=plt.cm.Blues):
    fig, ax = plt.subplots()
    im = ax.imshow(cm, interpolation='nearest', cmap=cmap)
    ax.figure.colorbar(im, ax=ax)
    # 注意这里的修改：x轴标签设置为预测标签，y轴标签设置为真实标签
    ax.set(xticks=np.arange(len(predicted_classes)), yticks=np.arange(len(true_classes)),
           xticklabels=predicted_classes, yticklabels=true_classes,
           title=title, xlabel='预测标签', ylabel='实际标签')

    # 绘制文本标签
    thresh = cm.max() / 2.
    for i in range(cm.shape[0]):
        for j in range(cm.shape[1]):
            ax.text(j, i, format(cm[i, j], '.2f'),
                    ha="center", va="center",
                    color="white" if cm[i, j] > thresh else "black")
    plt.tight_layout()

    # 旋转刻度标签以显示中文
    plt.xticks(rotation=45)
    plt.yticks(rotation=0)


# 绘制混淆矩阵
plot_confusion_matrix(conf_matrix, title='混淆矩阵')

# 显示图形
plt.show()
