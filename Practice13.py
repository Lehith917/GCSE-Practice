#Create a program that takes a list as input and sorts it using Bubble Sort algorithm. Print the list after each step.
list=[]
swapped=False
w=0
swaps=0
llen=int(input("Ente rhte number of items you want there to be in a list"))

for i in range(llen):
    item=float(input("Enter your item make sure its in random order"))
    list.append(item)
print(list)
while swapped==False:
    while w<llen-1:
        if list[w]>list[w+1]:
            temp=list[w]
            list[w]=list[w+1]
            list[w+1]=temp
            swaps=swaps+1
        print(list)
        
        w=w+1
        
    if swaps == 0:
        swapped=True
    else:
        w=0
        swaps=0