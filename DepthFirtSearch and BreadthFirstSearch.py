


NodeG3 = {
    "Name" : "G3",
    "NextNode3": None,
    "NextNode2": None,
    "NextNode1": None,
}

NodeG1 = {
    "Name" : "G1",
    "NextNode3": None,
    "NextNode2": None,
    "NextNode1": None,
}

NodeG2 = {
    "Name" : "G2",
    "NextNode3": None,
    "NextNode2": None,
    "NextNode1": None,
}

NodeB = {
    "Name" : "B",
    "NextNode1": {
        "Cost":9,
        "GetNode":NodeG3,
        },
    "NextNode3": None,
    "NextNode2": None,

}

NodeE = {
    "Name" : "E",
    "NextNode1": {
        "Cost":5,
        "GetNode":NodeG1,
        },
    "NextNode2": {
        "Cost":2,
        "GetNode":NodeG2,
        },
    "NextNode3": None,
}


NodeF = {
    "Name" : "F",
    "NextNode1": {
        "Cost":3,
        "GetNode":NodeG2,
        },
    "NextNode3": None,
    "NextNode2": None,

}



NodeA = {
    "Name" : "A",
    "NextNode1": {
        "Cost":6,
        "GetNode":NodeF,
        },
    "NextNode2": {
        "Cost":3,
        "GetNode":NodeE,
        },
    "NextNode3": None,
}

NodeD = {
    "Name" : "D",
    "NextNode1": {
        "Cost":2,
        "GetNode":NodeG3,
        },
    "NextNode2": {
        "Cost":2,
        "GetNode":NodeB,
        },
    "NextNode3": None,
}


NodeC = {
    "Name" : "C",
    "NextNode1": {
        "Cost":7,
        "GetNode":NodeD,
        },
    "NextNode2": {
        "Cost":2,
        "GetNode":NodeE,
        },
    "NextNode3": None,
}


NodeS = {
    "Name" : "S",
    "NextNode1": {
        "Cost":8,
        "GetNode":NodeB,
    },

    "NextNode2": {
            "Cost":3,
            "GetNode":NodeA,
        },

    "NextNode3": {
        "Cost":5,
        "GetNode":NodeC,
     },

}


def DepthFirtSearch(Goal:str,CurrentNode:vars,Path:list,BackTrackStorage:list,CheckedNode:list):
    if CurrentNode["Name"] != Goal:
        def NextNode(Name,CurrentNode):
            NewNode = CurrentNode[Name]["GetNode"]
            Path.append(NewNode["Name"])
            BackTrackStorage.append(NewNode)
            CheckedNode.append(NewNode)
            print(CurrentNode["Name"]+" TO "+NewNode["Name"])
            return NewNode,Path,BackTrackStorage,CheckedNode



        def CheckforPassedNode(Node,CheckedNode):
            for PN in CheckedNode:
                if PN == Node:
                    return True
            return False
        


        
        if CurrentNode["NextNode1"] != None and CheckforPassedNode(CurrentNode["NextNode1"]["GetNode"],CheckedNode) == False: 
            CurrentNode,Path,BackTrackStorage,CheckedNode = NextNode("NextNode1",CurrentNode)
        elif CurrentNode["NextNode2"] != None and CheckforPassedNode(CurrentNode["NextNode2"]["GetNode"],CheckedNode) == False:
            CurrentNode,Path,BackTrackStorage,CheckedNode = NextNode("NextNode2",CurrentNode)
        elif CurrentNode["NextNode3"] != None and CheckforPassedNode(CurrentNode["NextNode3"]["GetNode"],CheckedNode) == False:
            CurrentNode,Path,BackTrackStorage,CheckedNode = NextNode("NextNode3",CurrentNode)
        else:
            BackTrackStorage.remove(BackTrackStorage[len(BackTrackStorage)-1])
            CurrentNode = BackTrackStorage[len(BackTrackStorage)-1]
            Path.remove(Path[len(Path)-1])
            print("Back track")
        DepthFirtSearch(Goal,CurrentNode,Path,BackTrackStorage,CheckedNode)


    elif CurrentNode["Name"] == Goal:
        def GetAllCost(BacktrackList):
            Cost = 0
            for i in range(0,len(BacktrackList)-1):
                if BacktrackList[i]["NextNode1"] != None:
                    if BacktrackList[i]["NextNode1"]["GetNode"] == BacktrackList[i+1]:
                        Cost += BacktrackList[i]["NextNode1"]["Cost"]
                if BacktrackList[i]["NextNode2"] != None:
                    if BacktrackList[i]["NextNode2"]["GetNode"] == BacktrackList[i+1]:
                        Cost += BacktrackList[i]["NextNode2"]["Cost"]
                if BacktrackList[i]["NextNode3"] != None:
                    if BacktrackList[i]["NextNode3"]["GetNode"] == BacktrackList[i+1]:
                        Cost += BacktrackList[i]["NextNode3"]["Cost"]
            return Cost

        print("REACHED GOAL")
        print("path: ",Path)
        print("total Cost: ", GetAllCost(BackTrackStorage))
        return
    
DepthFirtSearch("G1",NodeS,[NodeS['Name']],[NodeS],[NodeS])





def BreadthFirstSearch(Goal:list,CurrentNode:vars,Path:list,Cost:int):
    Path.append(CurrentNode['Name'])
    if not CurrentNode["Name"] in Goal:
        if CurrentNode["NextNode1"] != None:
            NewCost = Cost + CurrentNode["NextNode1"]["Cost"]
            BreadthFirstSearch(Goal,CurrentNode["NextNode1"]["GetNode"],Path.copy(),NewCost)
        if CurrentNode["NextNode2"] != None:
            NewCost = Cost + CurrentNode["NextNode2"]["Cost"]
            BreadthFirstSearch(Goal,CurrentNode["NextNode2"]["GetNode"],Path.copy(),NewCost)
        if CurrentNode["NextNode3"] != None:
            NewCost = Cost + CurrentNode["NextNode3"]["Cost"]
            BreadthFirstSearch(Goal,CurrentNode["NextNode3"]["GetNode"],Path.copy(),NewCost)

    else:
        print("GoalReached")
        print(Path)
        print(Cost)

BreadthFirstSearch(["G1","G2","G3"],NodeS,[],0)