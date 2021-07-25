import requests
import json
from openpyxl import load_workbook
import pandas as pd

class WeatherForecast():
    def __init__(self):
        self.getWeather = "https://www.weatherol.cn/api/home/getCurrAnd15dAnd24h"
        self.header = {
            "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.212 Safari/537.36",
        }
        self.session = requests.session()

    # def getXuzhou(self):
    #     #只获取一个城市的天气预报
    #     # data = {
    #     #     'cityid': 101190801
    #     # }
    #     # r = self.session.get(url=self.getWeather,params=data,headers=self.header)
    #     # response = json.loads(r.text)
    #     # dic = response['data']['forecast15d']
    #     # index = ['XuZhou']*16
    #     # df = pd.DataFrame(dic,index=index)
    #     # df.to_excel('forecast.xlsx',sheet_name='XuZhou')
    #     '''
    #     获取多个城市的天气预报
    #     :return:
    #     '''
    #     # with pd.ExcelWriter('forecast.xlsx', engine='openpyxl', mode='a') as writer:
    #     data = {}
    #     cityid = {
    #         'Xuzhou':101190801,
    #         'Suzhou':101190101
    #     }
    #     lst = []
    #     for key,value in cityid.items():
    #         data['cityid'] = value
    #         r = self.session.get(url=self.getWeather, params=data, headers=self.header)
    #         response = json.loads(r.text)
    #         dic = response['data']['forecast15d']
    #         df = pd.DataFrame(dic,index=[key]*16)
    #         lst.append(df)
    #     total_df = pd.concat(lst)
    #     # print(total_df.head(5),df.dtypes,df.shape,df.info(),df.index,df.columns)
    #     total_df.to_excel('forecast.xlsx')

    def getXuzhou(self):
        # 只获取一个城市的天气预报
        # data = {
        #     'cityid': 101190801
        # }
        # r = self.session.get(url=self.getWeather,params=data,headers=self.header)
        # response = json.loads(r.text)
        # dic = response['data']['forecast15d']
        # index = ['XuZhou']*16
        # df = pd.DataFrame(dic,index=index)
        # df.to_excel('forecast.xlsx',sheet_name='XuZhou')
        '''
        获取多个城市的天气预报  按行加到已有的sheet表中
        :return:
        '''
        # with pd.ExcelWriter('forecast.xlsx', engine='openpyxl', mode='a') as writer:
        data = {}
        cityid = {
            'Xuzhou': 101190801,
            'Suzhou': 101190101
        }
        writer = pd.ExcelWriter('forecastss.xlsx')
        i = 0
        for key, value in cityid.items():
            data['cityid'] = value
            r = self.session.get(url=self.getWeather, params=data, headers=self.header)
            response = json.loads(r.text)
            dic = response['data']['forecast15d']
            df = pd.DataFrame(dic, index=[key] * 16)
            df.to_excel(writer,startrow=i*16)
            i+=1
        writer.save()

a = WeatherForecast()
a.getXuzhou()





