import numpy as np
import librosa
import librosa.output
import pickle
import librosa.segment
import librosa.display
import random
oo=5000000000000
# https://mhy12345.xyz/tutorials/librosa-samples/
# path = input("Path>")
# if not path:
#     path = "test.mp3"
# y, sr = librosa.load(path)
# y_harmonic, y_percussive = librosa.effects.hpss(y)
# tempo, beat_frames = librosa.beat.beat_track(y=y_percussive, sr=sr)
# with open("temp.pkl","wb") as f:
#     pickle.dump([y,sr,y_harmonic,y_percussive,tempo,beat_frames],f)
with open("temp.pkl", "rb") as f:
    y, sr, y_harmonic, y_percussive, tempo, beat_frames = pickle.load(f)
# 淡入淡出部分重叠？
# 每一段开始结束响度一样？
time = librosa.get_duration(y=y, sr=sr)
total_beat = librosa.time_to_frames(time)
# print((time,total_beat,beat_frames))
print(sr)
begin = 0
parts = []
last=0
for i in beat_frames:
    end = int((len(y)*i)/total_beat)  # +(sr)//120
    # print(i)
    # sum=0
    # for i in y[begin:end]:
    #     sum+=i
    # 平均值是没有意义的！！！！！！！！！！！！！！！！
    # 眼睛啦
    # 简单过0频率检测
    times = 0
    for i in range(end-begin):
        j=i+begin
        if (y[j-1] < 0 and y[j+1] > 1) or (y[j+1] < 0 and y[j-1] > 0) or y[j] == 0:
            times += 1
    this=times/(end-begin)
    parts.append([y[begin:end],this ,last])#Data, f of this ,f of last?  从后往前推
    last=this
    begin = end
#旧版本，选择可能性最高的，但是可能会造成死循环
# print(parts)
# ans = np.arange(1,dtype="float64")
# # ans[0]=parts[0]
# last=parts[0][1]
# now=parts[-1]
# for i in range(600,0,-1):
#     # print(i)
#     mymin=oo
#     go=0
#     for k in parts:
#         if abs(k[1]-now[2]) < mymin and k[1]-now[2] != 0 and not (k in ans):
#             mymin=abs(k[1]-now[2])
#             best_choice=k
#             go=1
#     if go == 0:
#         print("-----")
#         break
#     now=best_choice
#     # print(best_choice)
#     print(best_choice)
#     ans=np.append(best_choice[0],ans)

# print(ans)
# librosa.output.write_wav("loop2"+".wav", y=ans, sr=sr)

class myrandom_():
    def __init__(self):
        self.count=0
    def choice(self,mylist):
        self.count+=1
        return mylist[self.count%len(mylist)]

myrandom=myrandom_()
#新版本，正在编写，思路是：选出可能性醉倒的5（或者其他）个，然后DFS或者递推 有点KNN的感觉  无相连通图？
#最初的思路，没有进行算法优化
# print(parts)
ans = np.arange(1,dtype="float64")
# ans[0]=parts[0]
first=random.choice(parts)
now=first
cache={}
for i in range(600,0,-1):
    # print(i)
    distance={}#距离数组
    for k in parts:
        distance[abs(now[2]-k[1])]=k[0]#0不是1
    after_sort_key=sorted(distance.keys())
    indexx=random.choice(after_sort_key[:5])#还是不能用取余做随机，否则还是会重复
    # print(distance[indexx])
    ans=np.append(distance[indexx],ans)



    

# print(ans)
librosa.output.write_wav("loop2"+".wav", y=ans, sr=sr)
