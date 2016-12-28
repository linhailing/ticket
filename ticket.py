# -*- coding: utf-8 -*-
import requests
import json
import time

# 忽略 ssl 证书验证
# ssl._create_default_https_context = ssl._create_unverified_context

TRANT = 'G7028'
DATE = '2017-01-23'
DELAY = 300
FROM = 'SHH'
TO = 'TSJ'

'''
这个软件的功能是查询12306有没有余票
'''


# 查询余票
def select_ticket():
    url = "https://kyfw.12306.cn/otn/leftTicket\
/queryZ?leftTicketDTO.train_date={}&leftTicketDTO.from_station=\
{}&leftTicketDTO.to_station={}&purpose_codes=ADULT".format(DATE, FROM, TO)
    req = requests.get(url, verify=False)
    if req:
        print("请求成功")
    # 取出网页类容
    return req.text


# 转换json数据
def get_data(data_info):
    # data_info = self.select_ticket(self.url)
    info_json = json.loads(data_info)
    info = info_json['data']
    # 遍历每车次信息
    for train_data in info:
        # 判断获取需要查询车次的信息
        trains = train_data['queryLeftNewDTO']
        if trains:
            print("起始站:", trains['start_station_name'], end='   ')
            print("车次:", trains['station_train_code'], end='   ')
            print("商务座:", trains['swz_num'], end='   ')
            print("特等座:", trains['tz_num'], end='   ')
            print("一等座:", trains['zy_num'], end='   ')
            print("二等座:", trains['ze_num'], end='   ')
            print("高级软卧:", trains['gr_num'], end='   ')
            print("软卧:", trains['rw_num'], end='   ')
            print("硬卧:", trains['yw_num'], end='   ')
            print("软座:", trains['rz_num'], end='   ')
            print("硬座:", trains['yz_num'], end='   ')
            print("无座:", trains['wz_num'], end='   ')
            print("其他:", trains['qt_num'], end='   ')
            print("终点站:", trains['end_station_name'], end='   ')
            print("*" * 100)
# 循环查询
while True:
    html_info = select_ticket()
    get_data(html_info)
    print("-" * 100)
    # 延迟设定
    time.sleep(10)
