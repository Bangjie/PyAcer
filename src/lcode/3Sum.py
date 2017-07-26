
#coding:utf-8
'''


@author: xuzhi
'''


import copy

class Solution(object):
    
    ##time limit exceed
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        tu=[]
        for k in range(len(nums)):
            a=nums[k]
            for i in range(k+1,len(nums)):
                b=nums[i]
                for j in range(i+1,len(nums)):
                    c=nums[j]
                    if a+b+c==0:
                        t=[a,b,c]
                        if self.lel(tu,t):
                            tu.append(t)
        return tu
    
     
    def pd(self, t, ce):             # single element compare, same then True        
        i = 0
        e=copy.copy(ce)
        for tt in t :
            if tt in e:
                i += 1
                e.remove(tt)
                
        if i == 3:
            return True  
        return False
    
        
    def lel(self, tu, e):                #isornot in tu, not then False
        for t in tu:
            if self.pd(t, e):
                return False
    
        return True
    
    
    ##1、注意排序、两头并进，减少复杂度
    ##2、注意相同值的滑动，包括一、二、三
    ##3、注意滑动时，第一个值不能忽略
    def threeSumr(self, nums):
        nums.sort()
        print nums
        tu=[]
        
        for i in range(len(nums)):
            
            if i>0 and nums[i] == nums[i-1]:
               continue
#error!!
#             if i+1<len(nums) and nums[i] == nums[i+1]:
#                 continue
            
            l,r = i+1,len(nums)-1
            
            while l<r:
                s = nums[i]+nums[l]+nums[r]
                
                if s < 0:
                    l +=1
                elif s > 0:
                    r -=1
                else:
                    tu.append([nums[i],nums[l],nums[r]])
                    
                    while l < r and nums[l]==nums[l+1]:
                        l += 1
                    while l < r and nums[r]==nums[r-1]:
                        r -= 1
                        
                    l += 1
                    r -= 1
                    
        return tu
    
    
        
if __name__ == '__main__':
    s = Solution()
    nums =[-1, 0, 1, 2, -1, -4]
    nums2 = [-1,1]  
    nums3 = [0,3,0,1,1,-1,-5,-5,3,-3,-3,0]          
    
    print s.threeSumr(nums)
    
