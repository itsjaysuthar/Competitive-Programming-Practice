#---------------------------------------------------------------------------------------
#-------------------Author : itsjaysuthar ----------------------------------------------
#---------------------------------------------------------------------------------------


listt=[]
num = int(input())
for i in range(num):
    item = int(input())
    listt.append(item)

listt.sort()
for i in range(len(listt)):
    print(listt[i])