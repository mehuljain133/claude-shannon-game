import random
def graph_gen():
    graph={}
    q=random.randint(5,10)
    l=["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
    nodes=[]
    while len(nodes)<=(q-1):
        i=random.randint(0,25)
        x=l[i]
        if x not in nodes:
            nodes.append(x)    
    for i in nodes:
        r=random.randint(0,len(nodes)-1)
        y=[]
        for k in range(r+1):
            o=nodes[random.randint(0,len(nodes)-1)]
            if o not in y and o!=i:
                y.append(o)
            graph[i]=y    
    return graph   
