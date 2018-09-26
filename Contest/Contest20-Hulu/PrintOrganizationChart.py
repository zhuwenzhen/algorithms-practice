"""
997. Print Organization Chart
Give the Employee Name, Manager Name, Position, Year Hired as the relationships of the workers,
output the Corporate member organization chart.

Example
Give
relationship =[
    ["Karl","Nancy","Manager","2009"],
    ["Adam","Karl","Technician","2010"],
    ["Bob","Karl","Technician","2012"],
    ["Cathy","Wendy","Technician","2013"],
    ["Nancy","NULL","CEO","2007"],
    ["Wendy","Nancy","Manager","2012"]
    ]
return
    ["Nancy (CEO) 2007",
    "-Karl (Manager) 2009",
    "—Adam (Technician) 2010",
    "—Bob (Technician) 2012",
    "-Wendy (Manager) 2012",
    "—-Cathy (Technician) 2013"
    ]

Explanation:
Nancy's upper level is NULL,
so it is the highest level organization.
There are Karl and Wendy under Nancy, Adam and Bob under Karl, and Cathy under Wendy.

Give
relationship =
    [["Karl","Nancy","Manager","2009"],
    ["Nancy","NULL","CEO","2007"],
    ["Adam","Karl","Technician","2010"],
    ["Fred","Karl","Worker","2012"],
    ["John","Fred","Helper","2013"]
    ]

return
    ["Nancy (CEO) 2007","-Karl (Manager) 2009",
    "--Adam (Technician) 2010",
    "---Fred (Technician) 2012",
    "----John (Helper) 2013"]

Explanation:
Nancy is NULL at the next level and is therefore the highest level organization.
Karl has Nancy, Adam has Adam under Karl, Fred under Adam, and John under Fred.
"""


class Solution:
    """
    @param relationship: the relationship
    @return: the organization chart
    """

    def buildGraph(self, relationship):
        graph = {}
        for [_, boss, _, _] in relationship:
            graph[boss] = []
        for [worker, boss, _, _] in relationship:
            graph[boss].append(worker)
        return graph

    def buildTitleTable(self, relationship):
        table = {}
        for [worker, _, title, year] in relationship:
            table[worker] = [title, year]
        return table

    def getOrganization(self, relationship):

        g = self.buildGraph(relationship)
        print(g)

        boss = g["NULL"][0]
        queue = [boss]
        level_Table = {boss: 0}
        level = 0

        hsSet = set([boss])
        while queue:
            size = len(queue)
            level += 1
            for i in range(size):
                ppl = queue.pop()
                level_Table[ppl] = level
                for p in g[ppl]:
                    print(hsSet)
                    if not p in hsSet:
                        print(p)
                        hsSet.add(p)
                        queue.append(p)
        print("level", level_Table)


s = Solution()

relationship =[
    ["Karl","Nancy","Manager","2009"],
    ["Adam","Karl","Technician","2010"],
    ["Bob","Karl","Technician","2012"],
    ["Cathy","Wendy","Technician","2013"],
    ["Nancy","NULL","CEO","2007"],
    ["Wendy","Nancy","Manager","2012"]
    ]

s.getOrganization(relationship)