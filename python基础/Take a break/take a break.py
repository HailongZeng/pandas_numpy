import webbrowser
import time

total_breaks = 3
break_count = 0

print('This program started on' + time.ctime())
while(break_count < total_breaks):
    time.sleep(10)   # 2 hours
    webbrowser.open('https://www.youtube.com/playlist?list=PL_XbgoNYZT_AJxVpOXmM4Z53Rve02f8Sz') #爬虫案例
    break_count += 1
