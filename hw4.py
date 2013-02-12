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
    self.last = None

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
  def reverse(self):
    if self.length() == 1:
      return
    else:
      self.lastmaker()
      y = self.nexttolast()
      return y
  def lastmaker(self):
    if self.next != None:
      self.next.last = self
      self.next.lastmaker()   
  def nexttolast(self):
    if self.next == None:
      self.next, self.last = self.last, None
      return self
    else:
      self.next, self.last = self.last, self.next
      return self.last.nexttolast()
x = LinkedList(0, LinkedList(1, LinkedList(2, LinkedList(3))))
#x.reverse()
print x
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