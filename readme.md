# 说明
本人从2011年就是B站用户，对其ACG文化十分感兴趣<br>
该程序为抓取 https://www.bilibili.com/video/online.html ，即当前最高播放量的视频信息<br>
具体字段包括：视频名称，链接，作者，当前观看数，视频总播放量，弹幕数，具体步骤分为：<br>
1.请求发送<br>
2.使用Xpath方法进行数据解析<br>
3.保存到json<br>
4.统筹调用<br>
为便于信息查看，将json文件转化为了csv文件<br>
并且由于抓取后，部分信息包括汉字，所以又重新写了一段数据清洗方便的脚本，以便于后期分析用<br>
