from Knoten import Knoten
class Stack():
    def __init__(self):
      self.top = None
    def __repr__(self):
        items = []
        current = self.top
        while current:
            items.append(current.wert)
            current = current.next
        return str(items[::-1])
    def push(self, wert):
        neuer_knoten = Knoten(wert, self.top)
        self.top = neuer_knoten
    def pop(self):
        if self.top is None:
            return None

        wert = self.top.wert
        self.top = self.top.next
        return wert
    def peek(self):
        if self.top is None:
            return None
        return self.top.wert