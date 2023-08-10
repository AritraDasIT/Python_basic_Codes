import time
a=(time.strftime('%H:%M:%S'))
b=int(time.strftime("%H"))
c=int(time.strftime("%M"))
d=int(time.strftime("%S"))
print(a)
if(b>4 and b<12):
 print('Good morning')
elif(b>12 and b<18):
 print('Good evening')
else:
 print('Good night')