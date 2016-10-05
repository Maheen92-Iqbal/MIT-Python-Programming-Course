#we make the node with the value in it and then maintain its right and left branches
"""
node5 = BinaryTree(5)
node2 = BinaryTree(2)
node1 = BinaryTree(1)
node4 = BinaryTree(4)
node3 = BinaryTree(3)
node8 = BinaryTree(8)
node6 = BinaryTree(6)
node7 = BinaryTree(7)

node5.setLeftBranch(node2)
node2.setParent(node5)
node5.setRightBranch(node8)
node8.setParent(node5)
node2.setLeftBranch(node1)
node1.setParent(node2)
node2.setRightBranch(node4)
node4.setParent(node2)
node8.setLeftBranch(node6)
node6.setParent(node8)
node6.setRightBranch(node7)
node7.setParent(node6)
node4.setLeftBranch(node3)
node3.setParent(node4)

 """
class BinaryTree(object):
    
    def __init__(self,value):
        
        self.value = value
        self.leftBranch = None
        self.rightBranch = None
        self.parent = None
        
    def setLeftBranch(self, node):
        
        self.leftBranch = node
        return self.leftBranch
        
    def setRightBranch(self, node):
        
        self.rightBranch = node
        return self.rightBranch
    
    def setParent(self, node):
        
        self.parent = node
        return self.parent
            
    def getRightBranch(self):
        
        return self.rightBranch
        
    def getLeftBranch(self):
        
        return self.leftBranch
    
    def getParent(self):
        
        return self.parent
    
    def getValue(self):
        
        return self.value
        


def findNo6(node):
    
    return node.getValue() == 6
    

def DepthFirstSearch(root_node, func):
    
    stack = [root_node]
    
    while len(stack) > 0:
        
        if func(stack[0]):
            
           print 'At node {0}'.format(stack[0].getValue())
            
           return True               
                
        else:
            
            temp = stack.pop(0)
            
            print 'At node {0}'.format(temp.getValue())
            
            if temp.getRightBranch():
                
               stack.insert(0, temp.getRightBranch())
               
            if temp.getLeftBranch():
                
                stack.insert(0, temp.getLeftBranch())
                
    return False
    

def BreadthFirstSearch(root_node, func):
    
    queue = [root_node]
    
    while len(queue) > 0:
        
        if func(queue[0]):
            
            print 'At node {0}'.format(queue[0].getValue())
            
            return True
            
        else:
            
            temp = queue.pop(0)
            
            print 'At node {0}'.format(temp.getValue())
            
            if temp.getLeftBranch():
                
                queue.append(temp.getLeftBranch()) 
                
            if temp.getRightBranch():
                
                queue.append(temp.getRightBranch())
                
    return False
    

def DFSTracepath(root_node, func):
    
    stack = [root_node]
    
    while len(stack) > 0:
        
        if func(stack[0]):
            
            return Tracepath(stack[0])             
                
        else:
            
            temp = stack.pop(0)
            
            if temp.getRightBranch():
                
               stack.insert(0, temp.getRightBranch())
               
            if temp.getLeftBranch():
                
                stack.insert(0, temp.getLeftBranch())
                
    return False 
    

def Tracepath(node):
    
   if not node.getParent():
       
      return [node.getValue()]
      
   else:
       
      return [node.getValue()] + Tracepath(node.getParent())
                     

            
            
            
            