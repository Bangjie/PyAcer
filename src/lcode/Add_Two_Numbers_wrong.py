#Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
#Output: 7 -> 0 -> 8
#
# Definition for singly-linked list.

#coding=utf-8

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
            
    def convert(self, obj ):                    #trans linklist or numbers
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
        
        nextadd=False
        head = ListNode(0)
        node = head 
        while 1:
            
            if l1==None or l2==None:
                if l1==None:
                    if nextadd ==False:
                        node.val = int(l2.val)
                        break
                    else:
                        node.val = int(l2.val) + 1
                        if node.val >= 10:
                            node.val = int(node.val) - 10
                            nextadd=True
                        break
                else:
                    if nextadd ==False:
                        node.val = l1
                        break
                    else:
                        node.val = int(l1.val) + 1
                        if node.val >= 10:
                            node.val = int(node.val) - 10
                            nextadd=True
                        break
                    
            if nextadd==False:
                node.val = l1.val + l2.val
                
                if node.val >= 10:
                    node.val = int(node.val) - 10
                    nextadd=True
                    
                node.next = ListNode(0)
                node = node.next
                l1=l1.next
                l2=l2.next
            else:
                print type(node),type(node.val),type(l1),type(l1.val),node.val,l1.val,l2.val
                node.val = int(l1.val) + int(l2.val) + 1
                    
                if node.val >= 10:
                    node.val = int(node.val) - 10
                    nextadd=True
                    
                node.next = ListNode(0)
                node = node.next                 
                l1=l1.next
                l2=l2.next
                
            if l1 == None and l2== None:
                node.next = None
                break
        
        return head

if __name__ == "__main__":    
    s = Solution()
    a=s.convert(1)
    b=s.convert(4)
    c=s.addTwoNumbers(a,b)
    
    s.readList(c)