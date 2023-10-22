
myqueue=list()
def enqueue(myqueue,element):
    myqueue.append(element)
def isempty(myqueue):
    if len(myqueue)==0:
        return True
    else:
        return False
def dequeue(myqueue):
    if isempty(myqueue):
        return f"queue is empty"
    else:
        return myqueue.pop()
def size(myqueue):
    return len(myqueue)
def peek(myqueue):
    if isempty(myqueue):
        print("queue is empty")
    else:
        return myqueue[0]

#object
myqueue=list()
#accessing attributes
#each person to be assigned a code as p1,p2,p3,....
element=input("enter person code to enetr into the queue:")
enqueue(myqueue,element)
print(element)
print("number of persons in the queue is ",size(myqueue))
element=input("enter person code to enetr into the queue:")
enqueue(myqueue,element)
print(element)
element=input("enter person code to enetr into the queue:")
enqueue(myqueue,element)
print(element)
element=input("enter person code to enetr into the queue:")
enqueue(myqueue,element)
print(element)
print("number of persons in the queue is ",size(myqueue))
print("person removed from queue is :",dequeue(myqueue))


