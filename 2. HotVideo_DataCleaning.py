import pandas as pd
df = pd.read_csv('hot_csv.csv')

video_total_danmu = list(df['video_danmu'])
video_total_danmu_new = []
for i in video_total_danmu:
    if i[-1] == '万':
        i = float(i[:-1])*10000
    video_total_danmu_new.append(i)
df['video_danmu'] = video_total_danmu_new

video_total_watch = list(df['video_total_watch'])
video_total_watch_new = []
for i in video_total_watch:
    if i[-1] == '万':
        i = float(i[:-1])*10000
    video_total_watch_new.append(i)
df['video_total_watch'] = video_total_watch_new

df.to_csv("hot_csv_cleaned.scv", sep = ",", index = False)