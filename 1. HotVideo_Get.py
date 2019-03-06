import requests
from lxml import etree
import json
import csv

class VideoSpider(object):
    def __init__(self):
        self.base_url = 'https://www.bilibili.com/video/online.html'
        self.headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.110 Safari/537.36'}
        self.data_list = []
    #1.发请求
    def send_request(self, url):
        data = requests.get(url, headers = self.headers).content.decode('utf-8')
        print(url)
        return data
    #2.数据解析
    def parse_xpath_data(self,data):
        parse_data = etree.HTML(data)    #用XPath解析，第一步先做变量转化
        # 1.解析出所有的video
        video_list = parse_data.xpath('//div[@class="ebox"]')
        # 2.解析出每个视频的信息
        for video in video_list:
            video_dict = {}
             # 视频名字
            video_dict['video_name'] = video.xpath('.//p[@class = "etitle"]/text()')[0]
            # 视频链接
            video_dict['video_url'] = 'https://www.bilibili.com' + video.xpath('//div[@class="ebox"]/a/@href')[0]
            # 视频作者
            video_dict['video_author'] = video.xpath('.//a[@class = "author"]/text()')[0]
             # 视频当前观看数
            video_dict['video_current_watch'] = video.xpath('.//p[@class = "ol"]/b/text()')[0]
             # 视频播放量
            video_dict['video_total_watch'] = video.xpath('.//span[@class="play"]/text()')[0].strip()
             # 视频弹幕数
            video_dict['video_danmu'] = video.xpath('.//span[@class="dm"] /text()')[0].strip()
            self.data_list.append(video_dict)
    # 3.保存数据为json与scv
    def save_data(self):
        json.dump(self.data_list, open("hot_video.json", 'w', encoding= 'utf-8'))

    #4.统筹调用
    def start(self):
        data = self.send_request(self.base_url)
        self.parse_xpath_data(data)
        self.save_data()

VideoSpider().start()

# json 中的数据 转换成 csv文件

# 1.分别 读取json文件, 创建csv文件
json_fp = open('hot_video.json', 'r')
csv_fp = open('hot_csv.csv', 'w', newline="", encoding= 'utf-8')
# 2.提出 表头 , 表内容
data_list = json.load(json_fp)  #表内容
sheet_title = data_list[0].keys()  #表头
sheet_data = []
for data in data_list:
    sheet_data.append(data.values())
# 3. csv 写入器
writer = csv.writer(csv_fp)
# 4. 写入表头
writer.writerow(sheet_title)
# 5. 写入内容
writer.writerows(sheet_data)
# 6. 关闭两个文件
json_fp.close()
csv_fp.close()