# 首先遍历建立next连接，和dict字典位置一一对映
# 再次遍历，根据dict位置建立random连接
class Solution:
    # 返回 RandomListNode
    def Clone(self, pHead):
        # write code here
        if pHead is None:
            return pHead
        p = pHead
        qHead= RandomListNode(p.label)
        q = qHead
        map = {p:q, None:None}
        p = p.next
        while p is not None:
            clone = RandomListNode(p.label)
            q.next = clone
            q = clone
            map[p] = q
            p = p.next
        p = pHead
        q = qHead
        while p is not None:
            q.random = map[p.random]
            p = p.next
            q = q.next
        return qHead
