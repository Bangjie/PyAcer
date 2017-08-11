
#coding=utf-8
'''
Created on 2017年7月31日

@author: xuzhi
'''


class Solution(object):
    
    def gentest_fab(self,max):
        n,a,b = 0,0,1
        while n<max:
            yield b
            a,b=b,a+b
            n += 1
    
    def gene(self,left,right,s,result):
#normal writer
#         if right==0:
#             result.append(s) 
#         if left > 0 :
#             self.gene(left-1,right,s+'(',result)
#         if right >0 and left < right:
#             self.gene(left,right-1,s+')',result)
        
        if not right:       result.append(s) 
        if left:    self.gene(left-1,right,s+'(',result)
        if left < right:    self.gene(left,right-1,s+')',result)
                
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        s=''
        result=[]
        self.gene(n,n,s,result)
        
        return result
    
    def generateParenthesis2(self, n):
        def generate(p, left, right, parens=[]):
            if left:         generate(p + '(', left-1, right,parens)
            if right > left: generate(p + ')', left, right-1,parens)
            if not right:    parens.append(p),
            return parens
        
        return generate('', n, n)
    
    def generateParenthesis3(self, n):
        def generate(p, left, right):
            if right >= left >= 0:
                if not right:
                    yield p
                for q in generate(p + '(', left-1, right): yield q
                for q in generate(p + ')', left, right-1): yield q
        return list(generate('', n, n))    
    
    
    
    #error
    def generateParenthesis4(self, n,open=0):
        if n > 0 <= open:
            return ['(' + p for p in self.generateParenthesis(n-1,open+1)] + [')' + p for p in self.generateParenthesis(n, open-1)]
        return [')' * open] * (not n)    
    
if __name__ == '__main__':
    
    s=Solution()
    print s.generateParenthesis4(3)
    print list(s.gentest_fab(5))
    #print s.generateParenthesis2(3)
    