#coding=utf-8
'''
Created on 2017年8月7日

@author: xuzhi
'''
import copy

maze=[[1,0,1,1,0,1],
      [1,1,1,0,1,1],
      [0,0,1,0,1,0],
      [0,1,1,1,1,0],
      [0,0,0,1,0,0],
      [1,0,0,1,0,0]]

direction={'up':(-1,0),"down":(1,0),"left":(0,-1),"right":(0,1)}

allroute=[]
route=[]

def dfs((x,y)):
    
    if (x,y) in route:               #不走回头路
        return
    else:
        route.append((x,y))
        
    print x,y
    
    if maze[x][y]==0:
        
        print "no way!back from:",route.pop()
        return;
    
    
    if x==5 or x==0 or y==0 or y==5:
        
        print "Way Found!Sucess!Route:",route
        allroute.append(copy.deepcopy(route))
        return route.pop()
    
    dfs(move((x,y),direction['up'])) 
    dfs(move((x,y),direction['down'])) 
    dfs(move((x,y),direction['left']))
    dfs(move((x,y),direction['right']))
    
def move(loc,direction):
    return tuple(map(lambda x:x[0]+x[1],zip(loc,direction)))


if __name__ == '__main__':
    #print move((3,3),direction['right'])
    dfs((3,3))
    print "\nwe find %d routes"%len(allroute)
    print "allroute:",allroute
    