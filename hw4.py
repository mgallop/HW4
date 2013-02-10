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
#  def removeNodeByValue(self, value):
#    if self.head == value:
#      self.head = self.head.next
#    deletionHelper(value, self.head)
  def __str__(self):
    return printll(self.head)
    
def printll(start, text = "["):
  if start.next == None:
    text += str(start.value) + "]"
    return str(text)
  else:
    text += str(start.value) + ", "
    printll(start.next, text)
def deletionHelper(value, start):
    if start.next == None:
      return
    elif start.next.value == value:
      start.next = start.next.next
    else:
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