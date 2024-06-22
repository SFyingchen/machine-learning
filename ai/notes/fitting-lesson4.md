### 数据分割
将数据分割为训练集train_data、验证集validation_data 和测试集test_data。
CROSS_VALIDATION 交叉验证
###  数值归一化与标准化 Normalization standardize
+ 最大最小归一化 MinMaxScaler  什么时候使用？数据很大或者很小的时候使用
$$X_{norm} = \frac{X - X_{min}}{X_{max} - X_{min}}$$
+ 标准化 StandardScaler  什么时候使用？数据很密集的时候使用
$$X_{std} = \frac{X - \mu}{\sigma}$$
+ 还有一种 log 标准化   --> 让大数据变小

### one-hot Coding
####  不能直接用数字来表示类别  因为其之间是没有相关性的 仅是一种代表形式
但是：① 费空间 ② 计算扩展性差 ---->  使用 表征学习--embedding

### knn 算法
为什么要学习knn   
###  


