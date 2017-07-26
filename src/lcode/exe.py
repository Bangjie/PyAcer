need_field=['long_fundid','double_gainaby','double_riskaby']

import copy

c=[1,2,3]
    
def cc(c):
    b=copy.copy(c)
    b.remove(1)    
    
for i in c:
    print i
    cc(c)