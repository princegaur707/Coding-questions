class Solution:
    def destCity(self, paths: List[List[str]]) -> str:
        from collections import defaultdict
        dict1=defaultdict(set)
        for i in range(len(paths)):
            dict1[paths[i][0]].add(0)
            dict1[paths[i][1]].add(1)
        for key,value in dict1.items():
            value=list(value)
            if len(value)==1 and value[0]==1:
                return key
        return -1
        