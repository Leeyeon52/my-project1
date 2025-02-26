import time

stat_time = time.time()
'''print(time.time())
a = (time.localtime())
print(time.asctime)
print(time.ctime())

print(time.strftime('%Y/%B/%d %h:%M:%S',a))
'''


for i in range(10):
    time.sleep(1)
    print('출력')

end_time = time.time()
takes_time = end_time -stat_time
print('걸린시간:',takes_time)