import sys
sys.setrecursionlimit(10**6)

t = int(input())

def dfs(x, y):
    if x < 0 or x >= m or y < 0 or y >= n:
        return
    if L[x][y] == 0:
        return
    L[x][y] = 0
    dfs(x+1, y)
    dfs(x-1, y)
    dfs(x, y+1)
    dfs(x, y-1)

for i in range(t):
    m, n, k = map(int, input().split())
    L = [[0 for i in range(n)] for j in range(m)]
    count = 0
    for j in range(k):
        x, y = map(int, input().split())
        L[x][y] = 1
    
    for x in range(m):
        for y in range(n):
            if L[x][y] == 1:
                dfs(x, y)
                count += 1
    print(count)
        
