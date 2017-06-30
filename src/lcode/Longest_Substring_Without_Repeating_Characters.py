#coding=utf-8

class Solution(object):
    
    
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        
        
        i=0
        maxlen=0
        substr=''
        
        while i<len(s):
            index = substr.find(s[i])
            if index==-1:                            ##前进一个字符仍是满足条件的子串，生成新子串，步进值加一
                substr = substr + s[i]
                i=i+1
                
                if len(substr) > maxlen:
                    maxlen = len(substr)
            else:                                    ##前进一个字符不满足条件，记录长度，并向前进，生成新子串
                if len(substr) > maxlen:
                    maxlen = len(substr)
                    
                substr = substr[index+1:]+s[i]
                #print index,substr,maxlen,i
                i=i+1
        return maxlen
        
if __name__=="__main__":        
    s=Solution()
    print s.lengthOfLongestSubstring("auxauxk")