"""
Your task is to implement the Queue class with two basic operations:

    put(element), which puts an element at end of the queue;
    get(), which takes an element from the front of the queue and returns it as the result (the queue cannot be empty to successfully perform it.) 

Follow the hints:

    use a list as your storage (just like we did with the stack)
    put() should append elements to the beginning of the list, while get() should remove the elements from the end of the list;
    define a new exception named QueueError (choose an exception to derive it from) and raise it when get() tries to operate on an empty list.


"""

class QueueError(IndexError):
    pass


class Queue:
    def __init__(self):
        self.queue = []

    def put(self, elem):
        self.queue.insert(0, elem)

    def get(self):
        if len(self.queue) > 0:
            elem = self.queue[-1]
            del self.queue[-1]
            return elem
        else:
            raise QueueError


que = Queue()
que.put(1)
que.put("dog")
que.put(False)
try:
    for i in range(4):
        print(que.get())
except:
    print("Queue error")
    