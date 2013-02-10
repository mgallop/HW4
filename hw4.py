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