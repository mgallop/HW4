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
  def addNode(self, new_value): #class = O(n)
    if self.next == None:
      self.next = LinkedList(new_value)
    else:
      self.next.addNode(new_value)
  def addNodeAfter(self, new_value, after_node): #class = O(n)
    if NodeEqual(self, after_node):
      self.next = LinkedList(new_value, self.next)
    else:
      self.next.addNodeAfter(new_value, after_node)
  def addNodeBefore(self, new_value, before_node): #buggy
    if NodeEqual(self, before_node):
      self.next = LinkedList(self.value, self.next)
      self.value = new_value
    elif NodeEqual(self.next, before_node):
      self.next = LinkedList(new_value, before_node)
    else:
      self.next.addNodeBefore
  def length(self):
    if self.next == None:
      return 1
    else:
      return 1 + self.next.length()
  def __str__(self):
    if self.next == None:
      return "%r" % self.value
    else:
      return "%r, " % (self.value) + self.next.__str__()
  def removeNode(self, node_to_remove): 
    if NodeEqual(self, node_to_remove) and self.next == None:
      self.removeList()
    elif NodeEqual(self, node_to_remove):
      self.removeInitialNode()
    elif NodeEqual(self.next, node_to_remove):
      self.next = self.next.next
    else:
      self.next.removeNode(node_to_remove)
  def removeInitialNode(self):
    self.value = self.next.value
    self.next = self.next.next
  def removeNodeByValue(self, value):
    if self.next == None and self.value == value:
      self.removeList()
    elif self.next == None and self.value != value:
      return
    elif self.value == value:
      self.next.removeNodeByValue(value)
      self.removeInitialNode()
    else:
      if self.next.value == value:
        self.next = self.next.next
        self.removeNodeByValue(value)
      else:
        self.next.removeNodeByValue(value)
  def removeList(self):
    self.next = None
    self.value = None
#  def reverse(self):
#    self.head = reverser(self.head)
x = LinkedList(0)
x.removeNodeByValue(0)
print x
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
  elif node1.value == node2.value and (node1.next.value == None or node2.next.value == None):
    return False
  elif node1.value != node2.value:
    return False
  else:
    return True and NodeEqual(node1.next, node2.next)