import heapq

def h(a,b): return sum(abs(a.index(x)//3-b.index(x)//3)+abs(a.index(x)%3-b.index(x)%3) for x in a if x)

def astar(s,g):
    q=[(h(s,g),0,s,[])]; seen=set()  
    while q:
        f,d,u,p=heapq.heappop(q)
        if u==g: return p+[u]
        if tuple(u) in seen: continue
        seen.add(tuple(u))
        i=u.index(0)
        for m in [i-3,i+3,i-1,i+1]:
            if 0<=m<9 and not(i%3==0 and m==i-1) and not(i%3==2 and m==i+1):
                v=u[:]; v[i],v[m]=v[m],v[i]
                heapq.heappush(q,(d+1+h(v,g),d+1,v,p+[u]))

s=list(map(int,input("Initial path for order picking(9 nums): ").split()))
g=list(map(int,input("Goal path for order dropping(9 nums): ").split()))
path=astar(s,g)
for step in path:
    print(step[:3],"\n",step[3:6],"\n",step[6:],"\n")
print("Steps:",len(path)-1)
