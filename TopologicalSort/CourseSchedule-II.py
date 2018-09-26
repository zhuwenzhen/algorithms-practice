"""
616. Course Schedule II
There are a total of n courses you have to take, labeled from 0 to n - 1.
Some courses may have prerequisites, for example to take course 0 you have to first take course 1, which is expressed as a pair: [0,1]

Given the total number of courses and a list of prerequisite pairs, return the ordering of courses you should take to finish all courses.

There may be multiple correct orders, you just need to return one of them. If it is impossible to finish all courses, return an empty array.

Example
Given n = 2, prerequisites = [[1,0]]
Return [0,1]

Given n = 4, prerequisites = [1,0],[2,0],[3,1],[3,2]]
Return [0,1,2,3] or [0,2,1,3]
"""
import queue
class Solution:
    """
    @param: numCourses: a total of n courses
    @param: prerequisites: a list of prerequisite pairs
    @return: the course order
    """
    def findOrder(self, numCourses, prerequisites):
        if not numCourses: return []
        if not prerequisites: return [i for i in range(numCourses)]

        in_d = [0] * numCourses
        out_d = [[] for _ in range(numCourses)]
        # 1. Get in-degree for each course
        for p in prerequisites:
            in_d[p[0]] += 1
            out_d[p[1]].append(p[0])

        q = queue.Queue()
        # 2. for each course whose in-deg == 0, put it into queue as start
        for i in range(numCourses):
            if in_d[i] == 0:
                q.put(i)
        res = []
        # 3. Keep pop the queue
        while not q.empty():
            x = q.get()
            res.append(x)
            for node in out_d[x]:
                # other node's in-deg -1
                in_d[node] -= 1
                # if we find new node with in-degree is 0, put it back to queue
                if in_d[node] == 0:
                    q.put(node)

        if len(res) != numCourses: return []
        return res




n = 4
prerequisites = [[1,0],[2,0],[3,1],[3,2]]
s = Solution()
print(s.findOrder(n, prerequisites))