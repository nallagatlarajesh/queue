# write a python program to check whether 
# the given string is palindrome  or not ,using deque

string = input("enetr the string:")
deque=[]
for i in string:
    deque.append(i)
length =len(deque)//2
x=1
for i in range(length):
    front_element=deque.pop(0)
    rear_element=deque.pop()
    if front_element != rear_element:
        x=0
        break
if x==0:
    print("not palindrome")
else:
    print("palindrome")
