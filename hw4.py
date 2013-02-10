class Node:
  def __init__(self, _value=None, _next=None):
    self.value = _value
    self.next = _next
  def __str__(self):
    return str(self.value)
    
class LinkedList:
  def __init__(self, value):
    self.head = Node(value, None)
  def addNode(self, new_value):
    nextChange(None, Node(new_value), self.head)
  def addNodeAfter(self, new_value, after_node):
    nextChange(after_node.next, Node(new_value, after_node.next), self.head)
  def addNodeBefore(self, new_value, before_node):
    nextChange(before_node, Node(new_value, before_node), self.head)
  def removeNode(self, node_to_remove):
    nextChange(node_to_remove, node_to_remove.next, self.head)  
#Bug if trying to remove head node, for both removal methods
#    if NodeEqual(node_to_remove, self.head): 
#      self.head = self.head.next
  def removeNodeByValue(self, value):
    deletionHelper(value, self.head)
#  def __str__(self):
#    printll(self.head)


#Biggest Current Issue: Cannot get my recursive functions to return the right stuff
def listcounter(start, length=0):
  if start.next == None:
    printout = length + 1
    return printout
  else:
    length += 1
    listcounter(start.next, length)

def printll(start, text = "["):
  if start.next == None:
    text += "%d ]" % start.value
    printout = text
    return printout
  else:
    text += "%d, " % start.value
    printll(start.next, text)
def deletionHelper(value, start):
  if start.next == None:
    return
  if start.next.value == value:
    start.next = start.next.next
  if start.value == value:
    start = start.next  
  deletionHelper(value, start = start.next)

def nextChange(old, new, start):
  if NodeEqual(old, start.next):
    start.next = new
  else:
    nextChange(old, new, start.next)

def NodeEqual(node1, node2):
  if node1 == node2 == None: 
    return True
  elif node1 == None or node2 == None:
    return False
  elif node1.value == node2.value and node1.next == node2.next == None:
    return True
  elif node1.value == node2.value and node1.next.value == node2.next.value:
    return True
  else:
    return False