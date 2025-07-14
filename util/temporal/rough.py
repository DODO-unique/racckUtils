# serie={i:  for i in range(1,7)}
# # for i in range(1,7):
# #     serie[] = imperium % 100
# # print(serie)
imperium=550428_143817
# # serie={i:(imperium%100) if i<1 else imperium//100 for i in range(1,7)}

serie={}
for i in range(1,7):
    serie[i]=imperium%100
    imperium//=100
    


print(serie)
value=0
seconds=5150297
# seconds+=next(value+((365+(i % 4 ==0 and (i%100!=0 or i%400==0)))*86400) for i in range(serie[6]))
for i in range(serie[6]):
    value+=((365+(i % 4 ==0 and (i%100!=0 or i%400==0)))*86400)

seconds+=value
print(seconds)
