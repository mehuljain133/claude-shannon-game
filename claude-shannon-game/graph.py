import random
import graphmaker
import graphgen
class graphgame:
    def __init__(self):#Initialises the class variables
        self.graph={}
        self.possiblepaths=[]
        self.points=[]
        self.listofedges=[]
    def findpath(self,graph,start,end,path=[]):#Algorithm that finds the path/s between any 2 given points
        path=path+[start]
        if start==end:
             self.possiblepaths.append(path)
        elif start not in self.graph.keys():
            return None
        else:
            for node in self.graph[start]:
                if node not in path:
                    newpath=self.findpath(graph,node,end,path)
            return None
    def nodeselecter(self):#Selects the starting and ending nodes for the game randomly 
        l=[]
        for i in self.graph.keys():
            l.append(i)
        p=len(l)
        while len(self.points)<=1:
            i=random.randint(0,p-1)
            if l[i] not in self.points:
                self.points.append(l[i])
        return self.points
    def edgefinder(self):#Returns a list of all the edges that are present in the graph
        for i in self.graph.keys():
            for j in self.graph[i]:
                edge=str(i+j)
                self.listofedges.append(edge)
        return self.listofedges        
    def cutedge(self,de):#Removes the edges as per the rules of the game.
        deledge=de
        checklist=self.edgefinder()
        if deledge not in checklist:
            print("No such edge")
        else:
            d1=deledge[0]
            d2=deledge[1]
            for i in self.graph.keys():
                if d1==i:
                    for j in self.graph[i]:
                        if d2==j:
                            self.graph[i].remove(j)
 
def main():
    while True:
        new=graphgame()
        connecter=[]
        ce=[]
        print("--------------------------------------------------------------------------------------")
        print("\n\t 1.USE DEFAULT GRAPH \n\t 2.MAKE YOUR OWN GRAPH \n\t 3.GENARATE GRAPH")
        CH=int(input("Enter Choice:\n"))
        if CH==1:
            new.graph={"A":["B","C","D"],"B":["D"],"C":["E"],"D":["C"],"E":["A","B"]}
        elif CH==2:
            new.graph=graphmaker.graph_gen()
        elif CH==3:
            new.graph=graphgen.graph_gen()
        else:
            print("WRONG CHOICE. GOING WITH DEFAULT GRAPH")
            new.graph={"A":["B","C","D"],"B":["D"],"C":["E"],"D":["C"],"E":["A","B"]}
        t=[]
        t=new.nodeselecter()
        #t=["A","E"]
        new.findpath(new.graph,t[0],t[1])
        if len(new.possiblepaths)<2:
            print("SORRY FOR THE INCONVENINCE")
            print()
            continue
        else:
            print("----------------------------------------------------------------------------------")
            print("\t\t\t\tLet's begin the game!\n")
            print("\t\t\t\t---------------------\n")
            print()
            print("THE GRAPH: ",new.graph)
            print()
            print("The defined graph has the following edges:",new.edgefinder())
            del new.listofedges[:]
            print()
            print("Starting and end Point: ",t)
            print()
            print("ALL THE POSSIBLE PATHS IN THE BEGINNING: ",new.possiblepaths)
            print()
            turn=1
            while 1:
                if turn%2!=0:
                    print("---------------")
                    del new.possiblepaths[:]
                    new.findpath(new.graph,t[0],t[1])
                    if len(new.possiblepaths)== 0:
                        print()
                        print("There are no more paths possible, Slasher WINS!")
                        break
                    else:    
                        turn+=1
                        x=new.edgefinder()
                        print("Slashers turn:")
                        print("---------------")
                        print()
                        vu=[]
                        for j in x:
                            if j not in ce:
                                vu.append(j)
                        print("Available edges: ",vu)
                        de=input("Enter the edge you want to delete:")
                        if de in x and de not in ce:
                            new.cutedge(de)
                        else:
                            print("No such edge exists/It has already been marked. Try again")
                            turn=turn-1
                        del new.listofedges[:]
                        del new.possiblepaths[:]
                        print()
                        print()
                        print()
                elif turn%2==0:
                    flag=0
                    print("---------------")
                    del new.possiblepaths[:]
                    new.findpath(new.graph,t[0],t[1])
                    if len(new.possiblepaths)== 0:
                        print()
                        print("There are no more paths possible, Connecter LOSES!")
                        break
                    else:    
                        turn+=1
                        z=new.edgefinder()
                        print("Connecters turn:")
                        print("----------------")
                        print()
                        uv=[]
                        for i in z:
                            if i not in ce:
                                uv.append(i)
                        print("Available edges: ",uv)
                        se=input("Enter the edge you want to short:")
                        if se in uv :
                            ce.append(se)
                            if se[0] not in connecter:
                                connecter.append(se[0])
                            if se[1] not in connecter:    
                                connecter.append(se[1])
                            connecter.sort()
                            xt=new.possiblepaths[:]
                            for i in xt:
                                i.sort()
                                if i==connecter:
                                    print()
                                    print("Path completed. YOU WIN!")
                                    flag=1
                            if flag==1:
                                break
                        else:
                            print("No such edge exists. Try again")
                            turn=turn-1
                        
                        del new.listofedges[:]
                        del new.possiblepaths[:]
                        print()
                        print()
                        print()
                        print("----------------------------------------------------------------------------------")
            choice=input("What about another try at it??: y/n")
            if choice.lower()!="y":
                break
            
                        
                
                
            
        
        
        
        




















































































































































































