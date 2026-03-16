import numpy as np
import matplotlib.pyplot as plt

# プロットするデータを定義
x = np.arange(10)
y = x ** 2

# プロット
plt.plot(x, y)
plt.xlabel('x')  # x軸のラベル
plt.ylabel('y')  # y軸のラベル
plt.show()
