a= [['test_add_positive_numbers', 'PASSED'], ['test_add_negative_numbers', 'FAILED'],
    ['test_add_mixed_numbers', 'PASSED'], ['test_new', 'PASSED'], ['test_fail', 'FAILED'],
    ['test_add_positive_numbers', 'PASSED'], ['test_add_negative_numbers', 'PASSED'],
    ['test_add_mixed_numbers', 'PASSED'], ['test_new', 'PASSED'], ['test_fail', 'FAILED']]

d = {}

pass1 = 0
fail1 = 0
total1 = 0
# for i in a:
#       d[i[0]] = d1
for i in a:
   d1 = {'pass': 0, 'fail': 0, 'total': 0,'percentage':0}
       # print(d.items())
   if i[0] in d:
       if i[1]=="PASSED":
           d[i[0]]['pass'] = d[i[0]]['pass'] + 1
       elif i[1] == "FAILED":
           d[i[0]]['fail'] = d[i[0]]['fail'] +1
   else:
       d[i[0]] = d1
       # print(d)
       if i[1]=="PASSED":
           d[i[0]]['pass'] = 1

       elif i[1]=="FAILED":
           d[i[0]]['fail'] = 1

       # elif i[1] == "FAILED":
       #     d1[i[0]]['fail'] = fail1 + 1
   d[i[0]]['total'] = d[i[0]]['total'] + 1
   d[i[0]]['percentage'] = (d[i[0]]['pass']/d[i[0]]['total'])*100
print(d)
s = ["[['test_add_positive_numbers', 'PASSED'], ['test_add_negative_numbers', 'PASSED'], ['test_add_mixed_numbers', 'PASSED'], ['test_new', 'PASSED'], ['test_fail', 'FAILED']]",
"[['test_add_positive_numbers', 'PASSED'], ['test_add_negative_numbers', 'PASSED'], ['test_add_mixed_numbers', 'PASSED'], ['test_new', 'PASSED'], ['test_fail', 'FAILED']]"]
import ast
l = []
for i in s:
    l.extend(ast.literal_eval(i))

# print(l)