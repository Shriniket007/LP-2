import sys
visited = []
vertices = []
edges = []
h = []
cost=0
goal=0
n = int(input("Enter The number of vertices : "))
for i in range(n):
	vertices.append(str(input("Enter vertex : ")))

for i in range(n):
    print(vertices[i],": Enter the cost of the connected edge in the order of vertices above\n If edge exists: Enter cost\n If no edge: Enter 0")
    x=list(map(int,input().split()))
    edges.append(x)
print(edges)


for i in range(0,n):
	print(i+1,":",vertices[i],end="\n")

goal = int(input("Enter Goal State : "))-1
for i in range(0,n):
	print("Enter Hueristic value for : ",vertices[i],": ")
	h.append(int(input()))
visited.append(vertices[0])

def astar(i,iterations):
    global goal     #for not fixed goal
    global cost

    min = sys.maxsize
    minj = 0
    for j in range(iterations):
        if i[j] != 0 and vertices[j] not in visited:
            x = i[j] + h[j]                            # f(n) = g(n) + h(n)
            
            if x < min:
                
                min = x
                minj = j

    
    visited.append(vertices[minj])
    cost = cost + i[minj]
    
    if minj != goal:   #// we can use this only if we also take H[] as user input as H is different for different goal
        astar(edges[minj],iterations)
    else:
        print("Goal found.")

astar(edges[0],n)
print(visited)
print(cost)