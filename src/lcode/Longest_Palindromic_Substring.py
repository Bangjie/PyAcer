

class Solution(object):
    
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        maxlen = 0
        tmpstr = ''
        strlen = len(s)
        
        if strlen ==1:
            return s
        
        for i in range(0,strlen):

                        
            for k in range(0,1+ strlen/2):                 ## i as pivot, find palind string
                if i < k or i+k>=strlen:
                    break
                else:
                    if s[i+k] == s[i-k]:                        
                        tmplen=2*k+1
                        if tmplen > maxlen:
                            maxlen=tmplen
                            tmpstr=s[i-k:i+k+1]
                        #print tmpstr,maxlen,tmplen,i,k
                        
                    else:
                        break
                        
            for k in range(0,1+ strlen/2):                 ## i as pivot, find palind string  odd
                if i < k or i+k+1>=strlen:
                    break
                else:
                    if s[i+k+1] == s[i-k]:                        
                        tmplen=2*k+2
                        if tmplen > maxlen:
                            maxlen=tmplen
                            tmpstr=s[i-k:i+k+2]
                        #print tmpstr,maxlen,tmplen,i,k
                        
                    else:
                        break        
        return tmpstr
                        
if __name__ == "__main__":
    s=Solution()
    print s.longestPalindrome("babad")
    print s.longestPalindrome("abcda")
    print s.longestPalindrome("babadcbbd")
    print s.longestPalindrome("AAAA")
