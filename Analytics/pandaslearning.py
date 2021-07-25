import pandas as pd
import logging
logging.basicConfig(level=logging.INFO,format='%(lineno)d %(message)s')
'''
1,DataFrame和Series对象
note:（1）pd.Series.values 返回ndarray类型，可按列表遍历  pd.Series.index也可按列表遍历
(2)del pop删除列  drop删除行  append 添加行 通过标签定位loc 通过序号定位iloc 
'''
# lst = ['Echo','youngbeauty']
# index = ['person','who']
# s = pd.Series(lst,index=index)
#
# dic = {
#     'person':['Echo','Sky'],
#     'who':['female','male']
# }
# df = pd.DataFrame(dic,index=None)
# df['job'] = pd.Series(['SEng','HEng'])
# df['age'] = pd.Series([18,48])
# print(df['age'],type(df['age']),df,df.columns)
# # del df['job']
# # df.pop('person')
# # print(df)
# columns=['person','who','job','age']
# df2 = pd.DataFrame([['sam','male','leader',56],['sunny','female','pm',34]],
#                    columns=columns)
#
# df3 = pd.DataFrame([['gloria','female','l',22],
#                     ['yura','female','pm',28]],
#                    columns=columns)
# df = df.append([df2,df3])
# df.index = [1,2,3,4,5,6]
# print(df)
# # df = df.drop(0)
# # print(df)
# print(df.loc['1':'2','person':'who'])
# # df.set_index('person',inplace=True)
# print(df)
# df_new = df
# df_new = df_new.set_index('person')   #or  df_new.set_index(...,inplace=True)
# print(df_new)
# # df_new.to_excel('test.xlsx')
'''
2,数据组合
a,按行连接，用concat或append,参数为需连接的df组成的列表   
'''

