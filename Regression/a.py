listt = [1,2,2,3,4,5,5,3]
m = []
for i in range(0,len(listt)-1):
    if listt[i] == listt[i+1]:

        listt[i] = "a"
        listt[i+1] = "a"
        
# m = []
# for i in listt:
#     if i != "a":
#         m.append(i)
#
# print(m)
