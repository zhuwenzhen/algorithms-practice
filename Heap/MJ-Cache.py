"""
写一个数据结构Cache. visit 1point3acres for more.
Cache.set(time,key,value)
Cache.get(key)
time是这个key-value会在多长时间之后expire
get是在某个时间点get这个key，如果没有就返回none
我用的Priority Queue做的
就问了这一个题。。
"""

"""

这道题应该需要实时把过期的删除 直接的hashmap 空间需要过大
楼主应该是 PQ + hashmap 做的， PQ top是下个过期的，用来删除hashmap
Leetcode上类似的题目不含expire time，所以用普通的queue即可

对题目还有一个问题，每个key对应一个value with different expire time，
还是一个key对应多个value with different expire time。
如果是前者，map<key, [longest expire time, value]>貌似就可以
"""

