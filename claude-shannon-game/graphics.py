graph={"A":["B","C","D"],"B":["D"],"C":["E"],"D":["C"],"E":["A","B"]}
import random
l=[]
def findpath(graph,start,end,path=[]):
    path=path+[start]
    if start==end:
        l.append(path)
    elif start not in graph.keys():
        return None
    else:
        for node in graph[start]:
            if node not in path:
                newpath=findpath(graph,node,end,path)
            if newpath:
                return newpath
        return None

      
def nodeselecter():
    l=[]
    r=[]
    for i in graph.keys():
        l.append(i)
    print(l)
    p=len(l)
    while len(r)<=1:
        i=random.randint(0,p-1)
        if l[i] not in r:
            r.append(l[i])
    print(r)
def edgefinder():
    listofedges=[]
    for i in graph.keys():
        for j in graph[i]:
            edge=str(i+j)
            listofedges.append(edge)
    return listofedges
def cutedge():
    deledge=input("Enter the edge you want to delete:(eg.AB)")
    checklist=edgefinder()
    if deledge not in checklist:
        print("No such edge")
    else:
        d1=deledge[0]
        d2=deledge[1]
        for i in graph.keys():
            if d1==i:
                for j in graph[i]:
                    if d2==j:
                        graph[i].remove(j)    
    print(graph)
