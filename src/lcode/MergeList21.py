#coding:utf-8
'''
Created on 2017年7月28日

@author: xuzhi
'''
# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    
    def readList(self,l):
        
        if l==[]:
            return []
         
        a=[]
        while l != None:
            a.append(l.val)
            l=l.next
        
        return a
    
    def insertNode(self,l,node_val):
        tmp = l.next
        l.next = ListNode(node_val)
        l.next.next = tmp
    
    def listtoll(self,ls):
        ll=ListNode(0)
        head=ll
        for i in range(len(ls)):
            ll.val=ls[i]
            if i==len(ls)-1:
                ll.next = None
                return head
            else:
                ll.next=ListNode(0)
                ll=ll.next
                
        return head
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        from small to large
        """ 
        
        if l1 == [] or l2 == []:
            return l1 if l1 != [] else l2
                
        ll1=self.listtoll(l1)
        ll2=self.listtoll(l2)
            
        head,insertlist = (ll1,ll2) if ll1.val < ll2.val else (ll2,ll1)
        
        result = head 
        last = head
        while head != None and insertlist!= None:
            
            if head.val < insertlist.val:
                last = head
                head = head.next
                continue
            else:
                
                self.insertNode(last,insertlist.val)
                last = last.next
                
                insertlist = insertlist.next
        
        if insertlist!= None:
            last.next = insertlist
        return result

                    
if __name__ == '__main__':
    s=Solution()
    #l1=[1,3,6,9]
    #l2=[2,4,6,8]
    l1=[1]
    l2=[1]
    
    
    print s.readList(s.mergeTwoLists(l1, l2))
    