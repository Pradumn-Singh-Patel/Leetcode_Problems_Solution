# Leetcode Problems--Minimum Cost to Move Chips to The Same Position

class Solution(object):
    def minCostToMoveChips(self, chips):
        evenCount = oddCount = 0
        for chip in chips:
            if chip % 2 == 0:
                evenCount += 1
            else:
                oddCount += 1
        return min(evenCount, oddCount)
        
        