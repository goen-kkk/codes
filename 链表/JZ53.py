# 数字在升序数组中出现的次数
# 要求：空间复杂度 O(1)，时间复杂度 O(logn)

# @param data int整型一维数组 
# @param k int整型 
# @return int整型
#
class Solution:
    def GetNumberOfK(self , data: List[int], k: int) -> int:
        # write code here
        if len(data) == 0:
            return 0
        i = 0
        j = len(data)-1
        res = 0
        index = None
        while i <= j:
            index = (i+j) // 2
            if k < data[index]:
                j = index -1
            elif k > data[index]:
                i = index + 1
            else:
                break
        i = index - 1
        j = index
        while(j<len(data) and data[j]==k):
            res += 1
            j += 1
        while(i >=0 and data[i]==k):
            res += 1
            i -= 1
        return res
