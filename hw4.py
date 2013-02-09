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
    self.nextChange(None, Node(new_value), self.head)
  def addNodeAfter(self, new_value, after_node):
    after_node.next = Node(new_value, after_node.next)
  def addNodeBefore(self, new_value, before_node):
    self.nextChange(before_node, Node(new_value, before_node), self.head)
  def nextChange(self, old, new, start):
    if start.next == old:
      start.next = new
    else:
      nextChange(self, old, new, start.next)