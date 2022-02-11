"""

N = int(input())
book = []
book.append([])
visited = []
visited.append(1)
minPath = N+1
dist = [minPath]

for i in range(N):
    pp = input().split()
    if int(pp[0]) == 0:
        visited.append(0)
        book.append([0])
        dist.append(minPath)
        continue
    curlist = []
    for j in range(1, len(pp), 1):
        curlist.append(int(pp[j]))
    book.append(curlist)
    visited.append(0)
    dist.append(minPath)

stacklist = [1]
visited[1] = 1
dist[1] = 1

while len(stacklist) > 0:
    n = stacklist.pop()
    p = dist[n]
    for x in book[n]:
        if x == 0:
            if minPath > p:
                minPath = p
        else:
            if p+1 < dist[x]:
                dist[x] = p+1
                visited[x] = 0
            if visited[x] == 0:
                stacklist.append(x)
                visited[x] = 1

allvisited = True
for x in visited:
    if x == 0:
        allvisited = False
        break

if allvisited:
    print("Y")
else:
    print("N")
print(minPath)

"""





# keep an array of nodes. each index represents a page



class Node:
    def __init__(self, value):
        self.value = value # number
        self.children = [] # next pages

def getReachablePages(node, pages):
    if node.value not in pages:
        pages.add(node.value)
        for a in node.children:
            getReachablePages(a, pages)

def findShortestPath(nodesTocheck, level):
    level += 1
    childNodes = []

    for node in nodesTocheck:
        if len(node.children) == 0:
            return level
        else:
            for a in node.children:
                childNodes.append(a)
    return findShortestPath(childNodes, level)

totalPages = int(input())

#empty dictionary
pageMap = {}

for i in range(1, totalPages+1):
    pageMap[i] = Node(i)

for i in range(1, totalPages+1):
    line = input()
    d = line.split()
    d = list(map(int, d))

    for j in range(1, d[0] + 1):
        pageMap[i].children.append(pageMap[d[j]])

#look for all pages
pages = set()
getReachablePages(pageMap[1], pages)

if len(pages) == totalPages:
    print("Y")
else:
    print("N")

#get level

level = 0
nodesToCheck = [pageMap[1]]
print(findShortestPath(nodesToCheck, level))
