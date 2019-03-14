class node(object):
    def __init__ (self, index):
        self.nodes = []
        self.index = index
        self.discovered = False
    def addNode(self, index):
        self.nodes.append(index)

#read a graph in -> return a tree
def read_file(path):
    head = 0
    nodes = []
    with open(path, "r") as file:
        head = int(file.readline())
        index = -1
        node_i = None
        for edge in file.readlines():
            split1 = int(edge.split(',')[0])
            split2 = int(edge.split(',')[1])
            if(index == split1):
                node_i.addNode(split2)
            else:
                #previous node needs to be appended
                if(index != -1):
                    nodes.append(node_i)
                index = split1;
                node_i = node(split1)
                node_i.addNode(split2)
        #add last node
        nodes.append(node_i)
    return nodes[head]
            