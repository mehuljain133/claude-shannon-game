def graph_gen():
    graph={}
    l=["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
    while 1:
        x=input("Enter primary node:")
        y=[]
        while 1:
            z=input("Enter connected node: ")
            y.append(z)
            ch=input("Add another connection?: y/n")
            if ch.lower()!="y":
                break
            
        graph[x]=y    
        ch2=input("Want to add another primary node?:y/n")
        if ch2.lower()!="y":
            return graph
            break
            
                
