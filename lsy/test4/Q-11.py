from datetime import datetime

current_time = datetime.now()
print(type(current_time))
print('현재시간',current_time)

print(current_time.strftime('%Y/%m/%d %H/%M/%S'))


