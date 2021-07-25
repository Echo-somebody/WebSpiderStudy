import seaborn as sns
import os
import pandas as pd
import matplotlib.pyplot as plt

def df_I(a):
    return a == 'I'
def df_II(a):
    return a == 'II'
def df_III(a):
    return a == 'III'

path = r"D:\Users\Echo He\PycharmProjects\seaborn-data-master"
file = "anscombe.csv"
tips = "tips.csv"
filename = os.path.join(path,tips)
df = pd.read_csv(filename)
'''
df_I = df.loc[df['dataset'].apply(df_I)]  #DataFrame列的筛选
df_II = df.loc[df['dataset'].apply(df_II)]
df_III = df.loc[df['dataset'].apply(df_III)]

#创建画布用来放置子图
fig = plt.figure()
#指定子图的排布方式
axes1 = fig.add_subplot(2,2,1)
axes2 = fig.add_subplot(2,2,2)
axes3 = fig.add_subplot(2,2,3)
axes4 = fig.add_subplot(2,2,4)
axes1.plot(df_I['x'],df_I['y'],'o')
axes2.plot(df_II['x'],df_I['y'],'o')
axes3.plot(df_III['x'],df_I['y'],'o')
axes1.set_title('dataset1')
axes2.set_title('dataset2')
axes3.set_title('dataset3')
axes4.set_title('dataset4')
fig.suptitle('Anscombe Data')
fig.tight_layout()
plt.show()
# plt.plot(df['x'],df['y'])  #默认情况下画线，如果想要画原点，需要传递一个参数'o'
# plt.show()
# plt.plot(df['x'],df['y'],'o')
# plt.show()
# plt.plot(df_I['x'],df_I['y'],'o')
# plt.show()
'''
print(df)
'''
1,直方图单变量
'''
# total_bill = df['total_bill']
# fig = plt.figure()
# axes = fig.add_subplot(1,1,1)
# axes.hist(total_bill,bins=20)
# axes.set_xlabel('total bill')
# axes.set_ylabel('frenquency')
# axes.set_title('Hist of Total Bill')
# plt.show()

'''
2,箱线图 用于展现一个离散变量随连续变量的变化而呈现的分布状况
'''
# def df_female(a):
#     return a == 'Female'
# def df_male(a):
#     return a == 'Male'
#
# boxplot = plt.figure()
# axes = boxplot.add_subplot(1,1,1)
# print(df['sex'] == 'Female','\n',df[df['sex'] == 'Female'])
# df_female = df.loc[df['sex'].apply(df_female)]
# df_male = df.loc[df['sex'].apply(df_male)]
# # axes.boxplot(
# #     [df[df['sex']=='Female']['tip'],
# #      df[df['sex']=='Male']['tip']
# #     ],
# #     labels = ['Female','Male']
# # )
# axes.boxplot(
#     [df_female['tip'],
#      df_male['tip']
#     ],
#     labels = ['Female','Male']
# )

'''
3,多变量数据
'''
#基于性别创建一个带颜色的变量

# def reccord_sex(sex):
#     if sex == 'Female':
#         return 'red'
#     else:
#         return 'blue'
#
# df['sex_color'] = df['sex'].apply(reccord_sex)
#
# scatter_plot=plt.figure()
# axes = scatter_plot.add_subplot(1,1,1)
# axes.scatter(
#     x=df['total_bill'],
#     y=df['tip'],
#     s=df['size']*100,
#     c=df['sex_color'],
#     alpha=0.5
# )

'''
4,使用seaborn库  P56-P81略过
'''

plt.show()







