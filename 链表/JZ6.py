# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
#
# 代码中的类名、方法名、参数名已经指定，请勿修改，直接返回方法规定的值即可
#
# 
# @param listNode ListNode类 
# @return int整型一维数组
#
class Solution:
    def printListFromTailToHead(self , listNode: ListNode) -> List[int]:
        # write code here
        stack = []
        res = []
        if listNode == None:
            return res
        while listNode.next:
            stack.append(listNode.val)
            listNode = listNode.next
        stack.append(listNode.val)
        while len(stack) > 0:
            res.append(stack.pop())
        return res


import sys
#设置递归深度
sys.setrecursionlimit(100000)
class Solution2:
    def recursion(self, head: ListNode, res: List[int]):
        if head:
            self.recursion(head.next, res)
            res.append(head.val)

    def printListFromTailToHead(self , listNode: ListNode) -> List[int]:
        # write code here
        res = []
        self.recursion(listNode, res)
        return res
