class Queue:
    def __init__(self,value,priority):
        self.value = value
        self.priority = priority
        
class Priority:
    def __init__(self):
        self.queue = []
        
    def Length(self):
        return len(self.queue)
    
    def Enqueue(self,priority,elem):
        node = Queue(elem,priority)
        if len(self.queue) == 0:
            self.queue.append(node)
            return
        
        for i in range(0,len(self.queue)):
            if priority < self.queue[i].priority:
                self.queue.insert(i,node)
                return True
        
        self.queue.append(node)
        
    def Dequeue(self):
        aux = self.queue.pop(0)
        return aux.value
        
    def Search(self,position):
        i = 0
        for elem in self.queue:
            if [elem.value.x,elem.value.y] == position:
                return i
            i += 1