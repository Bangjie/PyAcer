#Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
#Output: 7 -> 0 -> 8
#
# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None
    
class Solution(object):
    
    @staticmethod
    def readList(l):
        node=l
        while 1:
            print node.val
            if node.next !=None:
                node=node.next
            else:
                break
            
    def convert(self, obj ):                    
        if(type(obj) != ListNode ):
            str_obj=str(obj)[::-1]
            length = len(str_obj)
            for i,v in enumerate(str_obj):

                if i==0:
                    node = ListNode(v)
                    head = node
                    last_node = node 
                elif i==length-1:
                    node = ListNode(v)
                    last_node.next = node
                else:                   
                    node = ListNode(v)              
                    last_node.next = node
                    last_node = node
                    
            return head    
        else:
            strl=''
            node=obj
            while 1:
                strl += str(node.val)
                if node.next != None:
                    node = node.next
                else:
                    break
            strl=strl[::-1]
            return int(strl)

    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        n1 = self.convert(l1)
        n2 = self.convert(l2)
        
        sn =n1 + n2
        
        return self.convert(sn)

if __name__ == "__main__" :       
    s = Solution()
    a=s.convert(3333333333)
    b=s.convert(46666666)
    c=s.addTwoNumbers(a,b)
    
    s.readList(c)