list=[]
find=float(input("What number do you want to find"))
found=False
upper=len(list)-1
lower=0
llen=int(input("Ente rhte number of items you want there to be in a list"))
for i in range(llen):
    item=float(input("Enter your item make sure its in lowest to highest order"))
    list.append(item)
upper=len(list)-1
while found==False and lower<=upper:
    mid=(lower+upper)//2
    if list[mid]==find:
        found=True 
        print(find,"was found in position:",mid)
    elif list[mid]>find:
        upper=mid-1
    else:
        lower=mid+1
if found==False:
    print("The number",find,"was not in the list.")

