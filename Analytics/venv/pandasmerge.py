import pandas as pd
import requests
import json
from openpyxl import load_workbook
import pandas as pd


# dic1 = {
#     'name':['echohe','skyli','sunny'],
#     'age':[10,40,30],
#     'gender':['female','male','female']
# }
#
# dic2 = {
#     'name': ['echohe', 'skyli'],
#     'score': [100, 120],
#     'weight': ['45kg', '60kg']
# }
# df1 = pd.DataFrame(dic1)
# df2 = pd.DataFrame(dic2)
# dic = pd.merge(df1,df2,how='left')
#
#
# df = pd.DataFrame(dic)
# df.to_excel('test.xlsx')

class WeatherForecast():
    def __init__(self):
        self.getWeather = "https://www.weatherol.cn/api/home/getCurrAnd15dAnd24h"
        self.header = {
            "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.212 Safari/537.36",
        }
        self.session = requests.session()

    def getXuzhou(self):
        # data = {
        #     'cityid': 101190801
        # }
        # r = self.session.get(url=self.getWeather,params=data,headers=self.header)
        # response = json.loads(r.text)
        # dic = response['data']['forecast15d']
        # df = pd.DataFrame(dic,index=['徐州','徐州','徐州','徐州','徐州','徐州','徐州','徐州','徐州','徐州',
        #                              '徐州','徐州','徐州','徐州','徐州','徐州'] )
        # df.to_excel('forecast.xlsx')
        # data = [{'cityid': 101190801},{'cityid': 101190101}]
        # for i in range(len(data)):
        #     r = self.session.get(url=self.getWeather, params=data[i], headers=self.header)
        #     response = json.loads(r.text)
        #     dic = response['data']['forecast15d']
        #     df = pd.DataFrame(dic)
        #     row = df.shape[1]*i-1
        #     print(row)
        #     df.to_excel('forecast.xlsx',startrow=row+1,header=False,index=False)
        # with pd.ExcelWriter('test.xlsx', engine='openpyxl', mode='a') as writer:
        #     data = [{'cityid': 101190801}, {'cityid': 101190101}]
        #     for i in range(len(data)):
        #         r = self.session.get(url=self.getWeather, params=data[i], headers=self.header)
        #         response = json.loads(r.text)
        #         dic = response['data']['forecast15d']
        #         df = pd.DataFrame(dic)
        #         row = df.shape[1] * i - 1
        #         print(row)
        #         df.to_excel('forecast.xlsx', startrow=row + 1, header=False, index=False)
        #
        #
        # writer.close()

        result2 = [('a', '2', 'ss'), ('b', '2', '33'), ('c', '4', 'bbb')]  # 需要新写入的数据
        df = pd.DataFrame(result2, columns=['xuhao', 'id', 'name'])  # 列表数据转为数据框
        df1 = pd.DataFrame(pd.read_excel('123.xlsx', sheet_name='Sheet1'))  # 读取原数据文件和表
        writer = pd.ExcelWriter('123.xlsx', engine='openpyxl')
        book = load_workbook('123.xlsx')
        writer.book = book
        writer.sheets = dict((ws.title, ws) for ws in book.worksheets)
        df_rows = df1.shape[0]  # 获取原数据的行数
        df.to_excel(writer, sheet_name='aa', startrow=df_rows + 1, index=False,
                    header=False)  # 将数据写入excel中的aa表,从第一个空行开始写
        writer.save()


a = WeatherForecast()
a.getXuzhou()

