"""
615. Course Schedule
There are a total of n courses you have to take,
labeled from 0 to n - 1.

Some courses may have prerequisites,
for example to take course 0 you have to first take course 1,
which is expressed as a pair: [0,1]

Given the total number of courses and a list of prerequisite pairs,
is it possible for you to finish all courses?

Example
Given n = 2, prerequisites = [[1,0]]
Return true

Given n = 2, prerequisites = [[1,0],[0,1]]
Return false
"""
import queue
class Solution:
    """
    @param: numCourses: a total of n courses
    @param: prerequisites: a list of prerequisite pairs
    @return: true if can finish all courses or false
    """
    def canFinish(self, numCourses, prerequisites):
        in_d = [0] * numCourses  # outdegree
        out_d= [[] for _ in range(numCourses)]  # indegree
        # 1. 统计每个点的入度
        for p in prerequisites:
            in_d[p[0]] += 1
            out_d[p[1]].append(p[0])
        q = queue.Queue()
        # 2. 将每个入度为 0 的点放入队列（Queue）中作为起始节点
        for i in range(numCourses):
            if in_d[i] == 0:
                q.put(i)
        k = 0
        # 3. 不断从队列中拿出一个点，
        # 去掉这个点的所有连边（指向其他点的边），
        while not q.empty():
            x = q.get()
            k += 1
            # 其他点的相应的入度 - 1
            for i in in_d[x]:
                in_d[i] -= 1
                # 一旦发现新的入度为 0 的点，丢回队列中
                if in_d[i] == 0:
                    q.put(i)
        return k == numCourses

    def canFinish2(self, numCourses, prerequisites):
        # initialize graph - use a dict to store the edges
        # {key = courseX, value = prereq for X}
        n = numCourses
        edges = {i: [] for i in range(n)}
        deg = [0 for i in range(n)]
        for i, j in prerequisites:
            edges[j].append(i)
            deg[i] += 1

        # use queue to hold courses
        import queue
        que = queue.Queue(maxsize=n)
        count = 0

        # init queue
        for i in range(n):
            if deg[i] == 0:
                que.put(i)

        # da zhao la
        while not que.empty():
            node = que.get()
            count += 1
            for i in edges[node]:
                deg[i] -= 1
                if deg[i] == 0:
                    que.put(i)
        return count == n

numCourses = 2
prereq = [[1,0], [0,1]]

s = Solution()
print(s.canFinish(numCourses, prereq))