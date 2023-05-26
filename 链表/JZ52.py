# 输入两个无环的单向链表，找出它们的第一个公共结点，如果没有公共节点则返回空。
# 时间O(n), 空间O(1)
# 先遍历一条链表，记录所有节点，再遍历第二条，找到第一个公共节点

# @param pHead1 ListNode类 
# @param pHead2 ListNode类 
# @return ListNode类
#
class Solution:
    def FindFirstCommonNode(self , pHead1 , pHead2 ):
        # write code here
        p = pHead1
        q = pHead2
        set_A = set()
        while(p!=None):
            set_A.add(p)
            p = p.next
        while(q!=None):
            if q in set_A:
                return q 
            q = q.next
        return None
        
