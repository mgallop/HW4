class Node:
  def __init__(self, _value=None, _next=None):
    self.value = _value
    self.next = _next
  def __str__(self):
    return str(self.value)
    
class LinkedList(Node):
  def __init__(self, value, next = None):
    self.value = value
    self.next = next
  def addNode(self, new_value):
    if self.next == None:
      self.next = LinkedList(new_value)
    else:
      self.next.addNode(new_value)
  def addNodeAfter(self, new_value, after_node):
    if NodeEqual(self, after_node):
      self.next = LinkedList(new_value, self.next)
    else:
      self.next.addNodeAfter(new_value, after_node)
  def addNodeBefore(self, new_value, before_node):
    if NodeEqual(self.next, before_node):
      self.next = LinkedList(new_value, before_node)
    else:
      self.next.addNodeBefore
#  def removeNode(self, node_to_remove):
#    if NodeEqual(self, node_to_remove):
#      self = self.next
#      self.removeNode(node_to_remove)
#    else:
#      self.nextChange(node_to_remove, node_to_remove.next)  
#Bug if trying to remove head node, for both removal methods
#    if NodeEqual(node_to_remove, self.head): 
#      self.head = self.head.next
#  def removeNodeByValue(self, value):
#    deletionHelper(value, self.head)
#  def __str__(self):
#    return "Under Construction!"
#  def length(self):

#  def reverse(self):
#    self.head = reverser(self.head)
    
#def reverser(start):
#  if start.next == None:
#    return start
#  else:
#    if start.next.next == None:
#      start.next.next = start
#      return start.next
#    else:
#      start.next.next = start
#      start.last = start.next
#      reverser(start.last)
#Biggest Current Issue: Cannot get my recursive functions to return the right stuff
def listcounter(start, length=1):
  if start.next == None:
    printout = length + 1
    print length
    return printout
  else:
    length += 1
    listcounter(start.next, length)


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