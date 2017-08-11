
# import copy
# 
# c=[1,2,3]
#     
# def cc(c):
#     b=copy.copy(c)
#     b.remove(1)    
#     
# for i in c:
#     print i
#     cc(c)
    
def binaryserch(nums,target):
    l,r = 0,len(nums)-1
    
    while(l<=r):
        mid=(l+r)/2
        
        if target == nums[mid]:
            return mid
        
        if target < nums[mid]:
            r=mid-1
        else:
            l=mid+1
        print "mid:",mid,r,l
        
    return -1


print binaryserch([1,2,3,4,5,8], 4)

        