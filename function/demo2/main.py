from datetime import datetime
from playsound import playsound

# 输入
alarm_time = input("请输入闹钟时间，实例：09:50:00 am\n")

# 时
alarm_hour = alarm_time[0:2]
# 分
alarm_min = alarm_time[3:5]
# 秒
alarm_second = alarm_time[6:8]
# AM or PM
alarm_period = alarm_time[9:11].upper()

print("success!alarm setted.")

while True:
  now = datetime.now()
  current_hour = now.strftime("%I")
  current_min = now.strftime("%M")
  current_second = now.strftime("%S")
  current_period = now.strftime("%p")

  if alarm_period == current_period and alarm_hour == current_hour and \
      alarm_min == current_min and alarm_second == current_second:
    print("时间到！")
    # music
    playsound('audio.mp3')
    break
