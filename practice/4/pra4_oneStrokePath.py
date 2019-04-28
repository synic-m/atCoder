N,M = map(int,input().split())
lis = [list(map(int,input().split())) for x in range(M)]

reached = [0 for x in range(N)]
graph = [[0 for x in range(8)] for y in range(8)]
def dfs(int v,int N,reached):
    all_visited = True

    for x in range(N):
        if reached[i] == 0:
            all_visited = false

    if all_visited == True:
        return
    ret = 0
     for x in range(N):
         if graph[v][x] == True:continue;
         if reached[i]==True:continue;

         reached[x] = True
         ret +=dfs(x,N,reached)
         reached[x] = False
    return ret


