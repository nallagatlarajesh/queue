#implementing of queue using python
#requiremets
#list data type
#enqueue :   2 parameters
               #name of the queue and
               # inserted element
               # append() function
#is empty :   1 parameter
                #name of the queue
                #len() function
#dequeue :  1 parameter :
                #name of the queue
                #returns delete element 
                #pop() function
#size    :    1 parameter 
                #name of the queue
                #returns length of the queue
                #len() function
#peek    :     1 parameter
                #name of the queue                        
                #  to read index[0]



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



                



