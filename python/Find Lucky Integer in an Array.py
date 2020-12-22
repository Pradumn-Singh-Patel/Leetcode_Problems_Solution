# Leetcode Problems--Find Lucky Integer in an Array

class Solution(object):
    def findLucky(self, a):
        a=Counter(a)
        b=[]
        d=[]
        e=[]
        for i in a.elements():
            b.append(i)
        for (i,j) in itertools.groupby(b):
            c=i,len(list(j))
            d.append(c)
        for i in d:
            if i[0]==i[1]:
                e.append(i[0])
        if e:
            return max(e)
        else:
            return '-1'